
using OfficeOpenXml;
using Spire.Xls;

namespace ImbScraper
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var info = Scraper.Scraper3000("https://www.imdb.com/chart/top/");
            //Escritorxml.EscribirExcel(info);
            Escritorxml.LeerExcel();

        }
    }
}
