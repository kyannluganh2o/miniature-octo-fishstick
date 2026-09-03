import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const here = path.dirname(fileURLToPath(import.meta.url));
const phaseDir = path.resolve(here, "..");
const tableDir = path.join(phaseDir, "tables");
const previewDir = path.join(process.env.TEMP || "C:/Windows/Temp", "phase14r_table_audit");
await fs.mkdir(previewDir, { recursive: true });

const tableIds = ["TAB-01", "TAB-02", "TAB-03", "TAB-04", "TAB-05", "TAB-06", "TAB-07", "TAB-08"];
const firstCsv = await fs.readFile(path.join(tableDir, `${tableIds[0]}.csv`), "utf8");
const workbook = await Workbook.fromCSV(firstCsv, { sheetName: tableIds[0] });

for (const tableId of tableIds.slice(1)) {
  const csvText = await fs.readFile(path.join(tableDir, `${tableId}.csv`), "utf8");
  await workbook.fromCSV(csvText, { sheetName: tableId });
}

const widthProfiles = {
  "TAB-01": [18, 28, 46, 42, 44],
  "TAB-02": [26, 28, 34, 24, 24, 25, 42, 34],
  "TAB-03": [24, 30, 22, 38, 25, 26, 25, 36, 38],
  "TAB-04": [24, 24, 34, 32, 34, 38, 40],
  "TAB-05": [26, 29, 30, 31, 34, 34, 34, 38, 40],
  "TAB-06": [22, 30, 36, 34, 36, 36, 39, 38],
  "TAB-07": [22, 30, 28, 30, 32, 34, 38, 35, 38],
  "TAB-08": [38, 42, 42, 45, 43, 43],
};

const summary = [];
for (const tableId of tableIds) {
  const sheet = workbook.worksheets.getItem(tableId);
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(1);
  const used = sheet.getUsedRange();
  const values = used.values;
  const rowCount = values.length;
  const colCount = values[0]?.length ?? 0;
  const endCol = String.fromCharCode(64 + colCount);
  const header = sheet.getRange(`A1:${endCol}1`);
  header.format = {
    fill: "#17324D",
    font: { bold: true, color: "#FFFFFF", size: 11 },
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "outside", style: "medium", color: "#17324D" },
  };
  header.format.rowHeight = 42;
  if (rowCount > 1) {
    const body = sheet.getRange(`A2:${endCol}${rowCount}`);
    body.format = {
      font: { color: "#16202A", size: 10 },
      verticalAlignment: "top",
      wrapText: true,
      borders: {
        insideHorizontal: { style: "thin", color: "#D8DEE5" },
        bottom: { style: "thin", color: "#AAB4BF" },
      },
    };
    body.format.rowHeight = tableId === "TAB-06" ? 82 : 72;
  }
  const widths = widthProfiles[tableId];
  for (let col = 0; col < colCount; col += 1) {
    sheet.getRange(`${String.fromCharCode(65 + col)}1:${String.fromCharCode(65 + col)}${rowCount}`).format.columnWidth = widths[col] ?? 30;
  }
  used.format.horizontalAlignment = "left";
  const table = sheet.tables.add(`A1:${endCol}${rowCount}`, true, `${tableId.replace("-", "")}Table`);
  table.style = "TableStyleMedium2";
  table.showBandedColumns = false;
  table.showFilterButton = true;

  const check = await workbook.inspect({
    kind: "table",
    range: `${tableId}!A1:${endCol}${Math.min(rowCount, 12)}`,
    include: "values,formulas",
    tableMaxRows: 12,
    tableMaxCols: colCount,
    maxChars: 3500,
  });
  summary.push(`${tableId}: ${rowCount - 1} data rows, ${colCount} columns`);
  console.log(check.ndjson);

  const preview = await workbook.render({ sheetName: tableId, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, `${tableId}.png`), new Uint8Array(await preview.arrayBuffer()));
}

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
  maxChars: 2500,
});
console.log(errors.ndjson);

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(path.join(previewDir, "phase14R_tables_audit.xlsx"));
console.log(summary.join("\n"));
console.log(path.join(previewDir, "phase14R_tables_audit.xlsx"));
