using HtmlAgilityPack;



namespace ImbScraper
{
    internal class Scraper
    {
        public static async Task<string> call_url(string url)
        {

            HttpClient client = new HttpClient();
            string response = await client.GetStringAsync(url);

            //Retorna todo el html
            return response;
        }

        public static List<string> Links(string html)
        {
            HtmlDocument document = new HtmlDocument();
            document.LoadHtml(html);
            List<string> linksList = new List<string>();
            var linkImb = "https://www.imdb.com";
            var tbody = document.DocumentNode.Descendants("tbody").Where(node => node.GetAttributeValue("class", "").Contains("lister-list")).ToList()[0];
            var tr = tbody.Descendants("tr").ToList();

            foreach (var node in tr)
            {
                var td = node.Descendants("td").Where(node => node.GetAttributeValue("class", "").Contains("titleColumn")).ToList()[0];
                var link = td.Descendants("a").ToList()[0].GetAttributeValue("href", "");
                linksList.Add(linkImb + link);
            }

            return linksList;

        }


        public static string Titulo(string html)
        {
            HtmlDocument document = new HtmlDocument();
            document.LoadHtml(html);
            var xpapthTitulo = "//*[@id=\"__next\"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span";
            var titulo = document.DocumentNode.SelectSingleNode(xpapthTitulo).InnerText;

            return titulo;
        }

        public static string TrimDato(string valor)
        {

            valor = valor.Remove(0, 1);

            return valor;

        }
        public static string Escritores(string html)
        {
            HtmlDocument document = new HtmlDocument();
            document.LoadHtml(html);

            var xpapthEscritores = "//*[@id=\"__next\"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[2]/div/div/div/ul/li[2]/div/ul";
            var liEscritores = document.DocumentNode.SelectSingleNode(xpapthEscritores).Descendants("li").ToList();
            string escritoresList = "";

            foreach (var node in liEscritores)
            {
                var nombre = node.Descendants("a").ToList()[0].InnerText;
                escritoresList += "," + nombre;
            }


            return TrimDato(escritoresList);

        }

        public static string Actores(string html)
        {
            HtmlDocument document = new HtmlDocument();
            document.LoadHtml(html);


            var xpapthActoresPrincipales = "//*[@id=\"__next\"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[2]/div/div/div/ul/li[3]/div/ul";
            var liActoresPrincipales = document.DocumentNode.SelectSingleNode(xpapthActoresPrincipales).Descendants("li").ToList();
            string actoresPrincipalesList = "";
            foreach (var node in liActoresPrincipales)
            {
                var nombre = node.Descendants("a").ToList()[0].InnerText;
                actoresPrincipalesList += "," + nombre;
            }


            return TrimDato(actoresPrincipalesList);

        }



        public static string Director(string html)
        {
            HtmlDocument document = new HtmlDocument();
            document.LoadHtml(html);
            var xpapthDirector = "//*[@id=\"__next\"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[2]/div/div/div/ul/li[1]/div/ul/li/a";
            var director = document.DocumentNode.SelectSingleNode(xpapthDirector).InnerText;

            return director;
        }


        public static string[,] Scraper3000(string url)
        {
            string[,] informacion = new string[250, 5];

            var html = Scraper.call_url(url).Result;

            var links = Scraper.Links(html);

            int fila = 0;
            foreach (var link in links)
            {

                var htmlPelicula = Scraper.call_url(link).Result;

                var titulo = Scraper.Titulo(htmlPelicula);
                var actoresprincipales = Scraper.Actores(htmlPelicula);
                var director = Scraper.Director(htmlPelicula);
                var escritores = Scraper.Escritores(htmlPelicula);

                informacion[fila, 0] = titulo;
                informacion[fila, 1] = director;
                informacion[fila, 2] = escritores;
                informacion[fila, 3] = actoresprincipales;
                informacion[fila, 4] = link;

                fila++;
            }

            return informacion;


        }



    }
}
