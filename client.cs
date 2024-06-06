using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // 서버 URL과 엔드포인트
        string url = "http://127.0.0.1:5000/login/create";

        // HttpClient 인스턴스 생성
        using (HttpClient client = new HttpClient())
        {
            // 요청할 때 보낼 파라미터 추가
            var parameters = new FormUrlEncodedContent(new[]
            {
                new KeyValuePair<string, string>("userID", "24028616486")
            });

            // 파라미터를 쿼리 문자열로 추가하여 URL 생성
            string requestUrl = $"{url}
	//?{await parameters.ReadAsStringAsync()}";

            // GET 요청 보내기
            HttpResponseMessage response = await client.GetAsync(requestUrl);

            // 응답이 성공적이면 내용 출력
            if (response.IsSuccessStatusCode)
            {
                string responseBody = await response.Content.ReadAsStringAsync();
                Console.WriteLine(responseBody);
            }
            else
            {
                Console.WriteLine($"Error: {response.StatusCode}");
            }
        }
    }
}

