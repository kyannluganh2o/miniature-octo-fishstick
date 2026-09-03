import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const root = path.resolve("../../..");
const phase14 = path.join(root, "08_Figures_Tables", "phase14");
const sources = [
  ["TAB-01", path.join(phase14, "tables", "TAB-01.csv")],
  ["TAB-02", path.join(phase14, "tables", "TAB-02.csv")],
  ["TAB-03", path.join(phase14, "tables", "TAB-03.csv")],
  ["TAB-04", path.join(phase14, "tables", "TAB-04.csv")],
  ["TAB-05", path.join(phase14, "tables", "TAB-05.csv")],
  ["TAB-06", path.join(phase14, "tables", "TAB-06.csv")],
  ["TAB-07", path.join(phase14, "tables", "TAB-07.csv")],
  ["TAB-08", path.join(phase14, "tables", "TAB-08.csv")],
  ["Quant Audit", path.join(phase14, "quantitative", "quantitative_eligibility_audit.csv")],
];

const firstText = (await fs.readFile(sources[0][1], "utf8")).replace(/^\uFEFF/, "");
const workbook = await Workbook.fromCSV(firstText, { sheetName: sources[0][0] });
for (const [sheetName, filePath] of sources.slice(1)) {
  const csvText = (await fs.readFile(filePath, "utf8")).replace(/^\uFEFF/, "");
  await workbook.fromCSV(csvText, { sheetName });
}

for (const [sheetName] of sources) {
  const sheet = workbook.worksheets.getItem(sheetName);
  const used = sheet.getUsedRange(true);
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(1);
  used.format = {
    font: { name: "Arial", size: 10, color: "#17324D" },
    verticalAlignment: "top",
    wrapText: true,
    borders: {
      insideHorizontal: { style: "thin", color: "#D9E1E7" },
      bottom: { style: "thin", color: "#D9E1E7" },
    },
  };
  used.format.columnWidth = sheetName === "Quant Audit" ? 20 : 24;
  used.format.rowHeight = sheetName === "Quant Audit" ? 100 : 88;
  const header = used.getRow(0);
  header.format = {
    fill: "#2F6690",
    font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "outside", style: "medium", color: "#17324D" },
  };
  header.format.rowHeight = 48;
}

const summary = await workbook.inspect({
  kind: "workbook,sheet,table",
  maxChars: 6000,
  tableMaxRows: 4,
  tableMaxCols: 6,
  tableMaxCellChars: 80,
});
console.log(summary.ndjson);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});
console.log(errors.ndjson);

const previewDir = "C:/Users/19451/.codex/visualizations/2026/09/02/01a060d6-f6dc-71e3-9f95-44e96fdbd755/phase14_table_previews";
await fs.mkdir(previewDir, { recursive: true });
for (const [sheetName] of sources) {
  const preview = await workbook.render({ sheetName, autoCrop: "all", scale: 0.8, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName.replaceAll(" ", "_")}.png`), Buffer.from(await preview.arrayBuffer()));
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(path.join(previewDir, "phase14_tables_audit.xlsx"));
console.log("saved phase14_tables_audit.xlsx");
