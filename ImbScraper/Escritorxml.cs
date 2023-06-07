using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Spire.Xls;

namespace ImbScraper
{
    internal class Escritorxml
    {

        public static void EscribirExcel(string[,] InformacionPeliculas)
        {

            //Create a Workbook instance
            Workbook workbook = new Workbook();
            //Remove default worksheets
            workbook.Worksheets.Clear();
            //Add a worksheet and name it
            Worksheet worksheet = workbook.Worksheets.Add("Peliculas");
            //Create a one-dimensional array
            string[] oneDimensionalArray = new string[] { "Titulo", "Director", "Escritores", "Actores Principales" , "Link"};
            //Write the array to the first row of the worksheet
            worksheet.InsertArray(oneDimensionalArray, 1, 1, false);

            //Write the array to the worksheet starting from the cell A3
            worksheet.InsertArray(InformacionPeliculas, 2, 1);
            //Auto fit column width in the located range
            worksheet.AllocatedRange.AutoFitColumns();
            //Save to an Excel file
            workbook.SaveToFile("C:\\Users\\yostin\\Desktop\\ImbScraper/Peliculas.xlsx", ExcelVersion.Version2016);
        }

        public static void LeerExcel()
        {
            //load an excel file from system    
            Workbook workbook = new Workbook();
            workbook.LoadFromFile("C:\\Users\\yostin\\Desktop\\ImbScraper/Peliculas.xlsx", ExcelVersion.Version2016);

            //find and highlight excel data    
            Worksheet sheet = workbook.Worksheets[0];
            foreach (CellRange range in sheet.FindAllString("Tim Robbins",true,true))
            {
                Console.WriteLine(range);
            }
        }

    }
}
