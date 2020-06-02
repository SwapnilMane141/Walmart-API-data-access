# -*- coding: utf-8 -*-
import scrapy
import json

class ApiTestSpider(scrapy.Spider):
    name = 'API_test'
    allowed_domains = ['grocery.walmart.com']
    start_urls = ['https://grocery.walmart.com/v3/api/cart/91a97db0-5b80-49f1-9c8c-bfeb2dc1d721/items']

    def parse(self, response):
        
        query=  {
                "cartItems":[
                    {
                        "offerId":"51CDBC4374C0490BAAD9C9214126D179",
                        "quantity":1
                    }
                ]
                }
        
        yield scrapy.Request(url='https://grocery.walmart.com/v3/api/cart/91a97db0-5b80-49f1-9c8c-bfeb2dc1d721/items',
                    callback=self.final,method='PUT',body=json.dumps(query),headers={
                        'content-type':'application/json',
                        'cookie':'vtc=bAEUwpgBVEeZnJTIALKD3M; _gcl_au=1.1.962060150.1591075214; viq=Walmart; s_vi=[CS]v1|2F6AF0C80515AEF7-4000063C00CE2825[CE]; WMP=4; oneapp_customer=true; ONEAPP_CUSTOMER=true; __gads=ID=ce08421213903999:T=1591075222:S=ALNI_MbMPRbx0EVcYNgq2QhsIJscegqevw; bstc=T0RqP4uEm-w2u-O__j7a6E; TS01af768b=01538efd7c7a1d94d73429d4ba874e4e78c3eefe2d2ea409b0390b42ca6f4bc41a339bbe42fc1582ff632734cf81750017c4e49135; TS012c809b=01538efd7c7a1d94d73429d4ba874e4e78c3eefe2d2ea409b0390b42ca6f4bc41a339bbe42fc1582ff632734cf81750017c4e49135; __cfduid=df9c096ed2029c08e1782be8adf425b841591113284; hasGCRT=1; TB_DNS_Perf_Test=1; TB_DC_Dist_Test=1; TB_DC_Flap_Test=1; mobileweb=0; ty-fe-env=n-blue; cart-fe-env=n-blue; xo-fe-env=n-blue; pac-fe-env=n-blue; thPillsWeb=true; go-xpa=6Ohhx|8ftLP|BnGdF|Bxmol|G3Z6T|GqhsP|Hhsz3|OSz3t|Spqwp|UL0-e|Uhvy5|UvvRW|Wt19z|YCiRs|aDi4V|lyrHR|qacLZ|vINoo|wW3CL|zOzKh; go-exp-ck=6Ohhx18ftLP1Bxmol1G3Z6T2GqhsP1Hhsz31UL0-e1Uhvy51Wt19z1lyrHR2; TS01e3f36f=01c5a4e2f9d9fba4d5a5575e3d26dca712181cb6ec736804bcfb621989e5dd8727da6ea790cdffd96421fd4fe8e11cc26f7e32aac9; TS018dc926=01c5a4e2f9d9fba4d5a5575e3d26dca712181cb6ec736804bcfb621989e5dd8727da6ea790cdffd96421fd4fe8e11cc26f7e32aac9; auth=MTAyOTYyMDE4gu55aMId3x29wCCYjTTIGchh%2FqWue5F%2FTH40SE1l2lLrgm3AcxBwBAWvp8XXvMWkH19XMyODM5%2FbdHRXvRwHh9oqqZ%2F%2FDd%2BnmLuczzUb3z%2BABuZPdeU1b5hhEBS%2BJVOlyc2e0wwmZvaRm87PQlkVaVWB4BkzDU4Jfl8GThDmYvIAlLd0nNOV%2BFT%2BuNYu7wKyb9O6gaVmm%2Bfx7A5ObCHtCz%2Bl3AeOul%2BzSsRNSF83bZcl462Il9IktR9z3xa%2FEqPEGq%2Bmp%2BP%2FcaxzgRYSMg3E7TUNgOjX3D2LEdNCTFD6j8JV1Y6qTjqXsJgmChnjomIzz36W9qqnXgI0gcFhoalnGpBU%2Fu8Rrlml5VhnQZP0GSC8aXYqmyXdeSmH%2FtVy74yg; rtoken=MDgyNTUyMDE4Vc%2B8HeO2TKveYBo1beyXtxeXirEIkjHqtFsmNCzXSNHzvLyX5dBgbHDeC8zI3XixY7%2BePgoMihDY7R%2BzguKdGAqdVMbQBhggVBLFYWTvx56oudDRc7ekLUDT%2BOCGtMbKpBLMYX2112v%2FeV2pBK2KC%2FmLRnMm6yfnLItv5k1m9jr9uwQqpt6hiFScKz71rNs1BjAwX4LlJLO8L6iEWgzcmR8ltylpjojGkQV%2FrqqV80e2g%2F7qL%2BC4I1tt5rTbjGRhftufOYqO5HN3l%2BkGsgAz%2BAcvSXCqN9hTAgj4G4WhJvUkPEz8J3PVfEeTROEC28irxVT%2BqJckj4UJ0UenkNRstBf7zlYnNMKFYxnnMKHCWciHK3NlQQyVN4fjcrttl1lyUJ5tzlnAwL%2F96aMLyJ5b9w%3D%3D; SPID=986146a6fd4bd5e165b63b6e929e6e13689ccb5de5d083559300d87b50f1bab2d674ff41a78478564655dc7d7116acd1myacc; CID=7fe2d60f-2356-44a0-b827-ac6e8e44db0c; hasCID=1; customer=%7B%22firstName%22%3A%22Test%22%2C%22lastNameInitial%22%3A%22S%22%2C%22rememberme%22%3Atrue%7D; type=REGISTERED; go-xpm=1%2B1591113453%2BbAEUwpgBVEeZnJTIALKD3M~%2B0; go-ty-fe-env=n-blue; go-cart-fe-env=n-blue; go-xo-fe-env=n-blue; go-pac-fe-env=n-blue; go-thPillsWeb=true; xpa=7Ivc1|UvvRW|onmki; exp-ck=onmki2; akavpau_gp2=1591114081~id=cbff64bc4bbae2aa2f8d3bed18e0158c; xpm=1%2B1591113481%2BbAEUwpgBVEeZnJTIALKD3M~7fe2d60f-2356-44a0-b827-ac6e8e44db0c%2B1; member=0; GCRT=91a97db0-5b80-49f1-9c8c-bfeb2dc1d721; TS01bae75b=01538efd7c4da1a64946f6e39755420411be989c1dc2d3aa8ec72909aaa7943136dd13bf469a52e813a00df0ffd45cb5a764e8b0c2; wm_mystore=Fe26.2**d9883848272eec81a33122c3488232be6e09829eca6bfaad57985f84a489f6af*BPJDjS5Os3Kv5J-lTHg6jA*-idvWpG_m7u_XaKrq-TNYyX6V4ZNXB8qtIqmG4g2JUM2Zlm10DdFUR5Ylu0FWtP0sANlI2HuxaVxjtMrZxsULJvajLSWwaEmB9Y0ukCp1SuC7iSPRyjVULmkd2SGZNWq4IW6zHOU0R2vTCrCUGAMe6bEYsjTYx4JQ5QS2dSHfQq1sCIRt6O2hYkUjncI4HvQOlnnhquOIveoAKw9frOseeEmPjJ5rR9AyBQ_hi-KJeCUn4ZidLpy01nZwnEu7T-qU9gGk1UD0I8XcEtjl8_ibYHXOrpJMbNxt6AYmuyPJCku6VmkD3GYwF6KyBJyR_WMC2VtNeNh69s483VJXZGnfQfnofz4WAUE4jdcCSE5z97LiR5iqGOly10eQ0iTtlvTaWyYWG4nvlV9lzN39Zs_O3cGHBiUnx_XaB8zL0Vu0nV1xYxE_08LhLD70EMiO6XpzDukYV7-mYE6xTFZJCZeNywDDOfugAvS8obuk9A3arQIwwN0ou0r4uCqeR-1FjQ4v2bApk1OnI2u_3eeMdNiEAAmx4vmz9b2bfv7uApae8BXXs3oEKFN4CzUYg5khZXO0-_3KcZ2G-6PYMOcAPRMib1um-4S1PQzWzT7IX2DJS6h0r5bI7CZ4qn2jfsQPYKFfMcrz0NWYtMoUMu4xN0BURPBoSSwrz24cur7fNjADKreb5xRyEBAEk7OUxLod0PxRCesfD9_pbOkAdJP0ZL6WmpJYmiNnfyAOCq-nDut1EM-5ZTP8I1PIYuoVL_4XGQgPeJcgVfYw98fjI4XKSIU0PT_tSpG9R0QRVa6WMrzbRCGCbGln2PQ3H_Fxfco8DzpZltKe5DGGiJ75k1teW8SLlSfhYkG5Rg2LY5p68Vq34k**249184e242f82983a3730fb4f5fe48c3fb9152e8ec48d88829dc376664ebf203*MaCinmTVMGOJembizisfmgOYVW39AsHTcSt8P8aaB_s; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiY29va2llIiwidXVpZCI6IjA2N2NkYmQwLWE0ZWEtMTFlYS05NWU5LWZiMmQzMmE3ODUwOCIsImlhdCI6MTU5MTExMzU2MiwiZXhwIjoxNTkyMTkzNTYyfQ.Fi4ert4LsGII0fOA2vTNAPPp59p4W-UUtv26-ymI8wk; akavpau_gp4=1591114163~id=ad802f0639399cef3d15c2ad0daaac15; TS01f4281b=01c5a4e2f941955e2d3c2f9319868e94fdaf34f5816ecc1b9816c29baa6ed80d68513a59f30839d018300c7b3c1c175eaa87c17a7e; TS01e1b9cb=01c5a4e2f941955e2d3c2f9319868e94fdaf34f5816ecc1b9816c29baa6ed80d68513a59f30839d018300c7b3c1c175eaa87c17a7e; TS01624fdb=01c5a4e2f941955e2d3c2f9319868e94fdaf34f5816ecc1b9816c29baa6ed80d68513a59f30839d018300c7b3c1c175eaa87c17a7e; s_pers=%20s_fid%3D5CB36F62FC5468A4-052F0C9BE69B3706%7C1654185600438%3B%20s_v%3DY%7C1591115400442%3B%20gpv_p11%3DPersistent%2520Cart%7C1591115400464%3B%20gpv_p44%3Dno%2520value%7C1591115400469%3B%20s_vs%3D1%7C1591115400475%3B; s_sess=%20ent%3DHomepage%3B%20s_cc%3Dtrue%3B%20cps%3D0%3B%20chan%3Dorg%3B%20v59%3D%3B%20v54%3DHomepage%3B%20s_sq%3D%3B',
                        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                        'wg-correlation-id':'60219410-a4e9-11ea-a807-b9e30d7fe127',
                        'x-csrf-jwt':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiaGVhZGVyIiwidXVpZCI6IjA2N2NkYmQwLWE0ZWEtMTFlYS05NWU5LWZiMmQzMmE3ODUwOCIsImlhdCI6MTU5MTExMzU2MiwiZXhwIjoxNTkyMTkzNTYyfQ.bk6H5R1Odayt_uoGwehpKM1-KwIKP8_P0MbXFqmrTfo'
                    })
        

    def final(self,response):
        print(response.body)

