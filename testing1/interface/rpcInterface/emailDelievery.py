import json, time, requests, random, sys, os

oridoc_1 = "UEsDBBQABgAIAAAAIQBvGmuQfgEAACgGAAATAAgCW0NvbnRlbnRfVHlwZXNdLnhtbCCiBAIooAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC0lM1qwzAQhO+FvoPRtdhKeiil2M6hP8c20PQBFGmdiNqSkDZ\/b9+145hSEocm+GIwZr+ZHY+UTrZVGa3BB21NxsbJiEVgpFXaLDL2NXuLH1kUUBglSmsgYzsIbJLf3qSznYMQ0bQJGVsiuifOg1xCJUJiHRj6UlhfCaRXv+BOyG+xAH4\/Gj1waQ2CwRhrBsvTDzLgtYJoKjy+i4p0+MZ6xQtr0ViEkBCORc\/7uVo6Y8K5UkuBZJyvjfojGtui0BKUlauKpJIa57yVEAKtVpVJh76r0TxPX6AQqxKj1y1528fhoQz\/U23XTGiycRaW2oUehf61Wmcn4+m268dckE5HroQ2B\/8nfQTclUP8oz33rDwYNVBJDuQ+CxTV1FsXOBXy6ppCXT4FKqauOvCooWvP6fQBkTo9wBkJLblv\/eacIp174M1zfHUGDeasZEF3wUzMS7ha78jV0KLPmtjA\/HOw9H\/B+4x0\/ZPWXxDG4caqp4+0jjf3fP4DAAD\/\/wMAUEsDBBQABgAIAAAAIQAekRq38wAAAE4CAAALAAgCX3JlbHMvLnJlbHMgogQCKKAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjJLbSgNBDIbvBd9hyH032woi0tneSKF3IusDhJnsAXc"
oridoc_2 = "OzKTavr2jILpQ217m9OfLT9abg5vUO6c8Bq9hWdWg2JtgR99reG23iwdQWchbmoJnDUfOsGlub9YvPJGUoTyMMaui4rOGQSQ+ImYzsKNchci+VLqQHEkJU4+RzBv1jKu6vsf0VwOamabaWQ1pZ+9AtcdYNl\/WDl03Gn4KZu\/Yy4kVyAdhb9kuYipsScZyjWop9SwabDDPJZ2RYqwKNuBpotX1RP9fi46FLAmhCYnP83x1nANaXg902aJ5x687HyFZLBZ9e\/tDg7MvaD4BAAD\/\/wMAUEsDBBQABgAIAAAAIQARF6DZFAEAADkEAAAcAAgBd29yZC9fcmVscy9kb2N1bWVudC54bWwucmVscyCiBAEooAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKyTy07DMBBF90j8gzV74qRAQahONwipWwgf4CaTh0g8kT088vdYkRJSqMLGG0tzLd97PGPv9l9dKz7QuoaMgiSKQaDJqWhMpeA1e7q6B+FYm0K3ZFDBgA726eXF7hlbzf6Qq5veCe9inIKauX+Q0uU1dtpF1KPxOyXZTrMvbSV7nb\/pCuUmjrfSLj0gPfEUh0KBPRTXILKh98n\/e1NZNjk+Uv7eoeEzEfITjy\/I7C\/nvK22FbKChRh5WpDnQe5CgrBvEP4gjKUc12SNYROSwf3pxKSsISRBEXho\/YOaR+HGei1+GzK+JMOZPraLSczSGsRtSAg0hSFedmFS1hBuQiKURPyLYZYmCHny4dNvAAAA\/\/8DAFBLAwQUAAYACAAAACEATorJOTUNAAAobwAAEQAAAHdvcmQvZG9jdW1lbnQueG1s7FzbU9vGGn8\/M\/0fGL+DdfNFTKGHa9uZnpkM7TnnWdgC3MqWKwkofSJJE1IKJTkN5AJpUjopbU5DgEC5Ne0\/Y8nyU\/+FfiutHK2xqCwsI3Uyw4zNrrT77e+77rff+u13PitKXTOiohbkUl+C7qESXWIpJ+cLpcm+xL8\/Gu3OJrpUTSjlBUkuiX2JOVFNvNP\/1j\/enu3Ny7npoljSumCIkto7A71TmlbuTSbV3JRYFNQeuSyWoHNCVoqCBv8qk8mioHwyXe7OycWyoBXGC1JBm0syFJVO4GHkvsS0UurFQ3QXCzlFVuUJDb3SK09MFHIi\/nDeUPzMa785jEm2ZkwqogQ0yCV1qlBWndGKQUeDJU45g8yct4iZouQ8N1v2M1teEWaBH0XJJntWVvJlRc6Jqgqtw3ZnfUSaOm9uDCAaov6GHxLIOR1KikKhVB8GSUcD\/+vM6wHmJe25k2io1wsBLPpBlsbl\/Bz61MYl\/HFFwV8+1OYksWu2d0aQ+hICm0ji9v9C22xfgmdTfAK+anNlICD\/mVB\/4P1S3n6km86AeDV7ZBBoAdm3RpTL8Ig1CYJVEtEb6uegE4z1rSzkYHxQj9nenCzJIHTCtCbbk0nihBb45XFZ0+Ri4NeVwuRU8MkLJbWQF98LPLv9\/n8Cvp+0GO5mwrj0gSx\/4gxHcQMUQth+ri4R7yqFPGLZJHwOyRI8DXJAc9mMzQ2iOYMFhmikGZZv8izLWLM1DMzzTJNnsym6SSuXbtaaYpu1ZrLNWmkW5M0ScZJi3Gwj8S4GQFNg7WC682MgmRRHpUYHRpGAoqaPQEIpaphhuFTWUjFNwQAq74lumaGRdmCQnUdylkbk8Au581UNEfphWSg5XKPxurScm7Ov1atUkOwVutWm3kjIM25Fq3YPNjMgFSbr8+XAB4mKswRMNFJmD2TGrljQDI4wzPCIA9fYsDghTEvaWSCvoCZmMJUeZSwcyzYqKhgEsBMwjVRApo8B4cH\/jE1L0CBoH4iCqtlL\/TjnoPOaWiAQD\/W508lanEB2Z0gl2wAC62n4xATUeU8sBzEOD6uMyiUNDTNVKMG6EDEDakGwCVJbmBPQ768cPbPU0FJGyzTX53fhA5NZoHeCJBQv9CIuA"
oridoc_3 = "NZlRVRFZUZM9Hd1eZHZCZr6KycnXvO\/gckRTK2\/uj3\/Biakqt6KjpRO\/\/omARNSftsbgoFGRtGOkc7RRN9eIJ2y3I41qGP2mzoBy8+CnjfEW62aZGxQHYPhsr5kT2jW12VI\/dlMeAEbVmDM1jf67WVv3gA8zV2o5d7PotfoQnEI0D5Q+SGOGhpGDgrZZwtU3IQW3zaXdiFQa9evVo4fmUvHMcI1DsJqzG\/pt\/4fI1CbCGsY8deFhLV69zBGiMZBTPWFk+rdx\/rxvrFxq33QhmpCIyeVNJ\/lCOzA3jsuFsWfLM+xwxlrG\/PXmwS3w+tpHLV1n0lTjWNEhTKGJyhDdqEeZbXqyWf+JSqT9XQVbEs0QcF7wPaJYofVmQAE\/mln2JmxkjbWoJcbdpLpgGiGndXdZXP\/RfuE9TLCzsjZTGPvpb58D\/5q91\/GCFpfNkATxu3ktjAOxtZKbqOkG9oHlGW1L5FJ1fOr+MmLp7WQtbBV2U4T4e\/eySh4ob6xMnbuGPdWYsSGOMSqxu6XMULUl2Bftpje\/d3YO6092jT3ltoHbfsChDhIpb6+qd+530b0rMjLOjppH5AdFkZkO+uhpxUUWTk4IoYnSfKf4MtEJcEXh0hLf\/7DucnXVrcFbyItSGcbGz9Xt+60T+NDBzUOklo5+qZy9DBGoMbBNxkbJ8bmjrn9m7n9XYygJV1DNPew+k8P9a3T6uIv+s2DANAyaYZD25eG46fQTUEcpFY\/3AN0vUH1CChIK+c7oMjYhSrWoJ1I3ZBkuus1yJ6Iiv3ujcqrFX1jR39EHn0TIZ9nWMHyUBry12KPy0dajX9JAN3QxkHsK0eLxsGhcfBD5WjDWNvRl84twWAHmUyKDZACN9aPq\/+7XVtdgByFOT9vHkYvEefNR7InmipiXr1bfXlqrB3rvwbJAIXrGUgA46YidIqnqCzPcym6ZfdABhW+3UOWrqcWneyeR0kEKtw8a9patWEkmW4GkT3RlH3jxSpE8bUHm8aTIAFnuO6BBNANbXqUZekBxL16WQl+ODplJfr2l42Z\/YZTUezkWj\/S1A+fQqIAuOatVJ4e\/bIqgUhmRlMbzK92zRfPjZ19\/TjIkUy4noAE0K0NcQiW9PX16smWt7x67BFSHMNmW68tT3NWnX3H9ggkmW7ekD3RFHtj47GxsW6uPTMPvvDmkKdFYblMqokjbdwap+wC8Fb9KwmgG9o4iH2Wos6Un7Ru7yunT2GzEYA16A7J2RCnkTMBqz69OUP2RFPoa9e2q9u7ATBl4b6LD1Dx\/Z\/2iTuuoYp0zMOmUzydTadS\/D8\/\/RRdvvPG18Pgk\/sd31H\/hQ1++8qnyBW4DRbZE021gNCy8mqjeroS8BgqzfqxOAGVgwQwbtAa936p3dv31ghPB0tnOdaHxQloxuMNqr68WnkV5EZEqK4x3piaV5f0xUDpgFBdY7xBtQ2rfvOGvn3ORRMPr0hzDD1o3fNE+Y4WvOIFc2HBS1tIit2mmuwJ3QsCoq9LW7xNbKh+i1yyGwwqk6JHrN8RiG4ii6Forodiu+EzS3ivhnQWXmXr25s2FPlTDEGZT6aH6le9mU72hK4BLjbZd5EDM8r8\/Zn+5Lvawh3z28i5XBJUt46RPZ2Au3UVQC43UFFiuLtREjo3qAxNc3xHDRfe+I7ZMoznbx1pfWXN+Pk3KLSpPvwCUvTm9zf++HXJ+H7eOPgKvpg7180Xq962xMM\/k6FJHPwzSbGbs2RP6Ori01SH6p\/JJbvBiIl\/zoJ\/JoTWZfPR\/bthKJoZ4gIUH3SHMqq5QB6vNFKbpvihkQDUQoTCJyMYCnjLF2ZMpJN6cBgGhtJ4sG1cf0KIgz\/VvaSNdhyQjajX9xbXOOSgq8\/XjcdP9e1N49YhHGiZ+z8SQgu2puWgweMnfy48br+xtGZ8fd+mtbYxb+xeaxzTiXqsW9QBS8h8kt+Oqfr15RV98Sd98dvq7Zvm\/iGEWsSKCJPhEUyRp0e+g6lMph3JDgDBuq54oRvU5Arc8QTZE3pwFUTY+43VB+a1PfP6kvEgUKlhqKEaCWDsoI3mEUADqPYOq6HR9UtJZE8nhNgxTQRlLZtx+DG5gHdWOJZvVivYeJDenhIHYpHOyv8O8EPNGpQZwg9YVbd24uUVAt3uJNXkEk0V4XQvKQXuDcZImsoMRbyWk4EqZkJiG3aswX\/fhsqivDrVkyaG98mxUPPX3hyLwy7AfZNOX1k0F57piz\/qS2sBYO6o8XfZ+TjAbBc5+6hHjmK"
oridoc_4 = "s\/ze36n8CAAD\/\/+xXbUvbUBT+K5I\/YJqXNi1rQaluHzYoOtjnmMY2IzYhvbW6TzJ1voxVZTBhFhy4Ishm2ZBVq92vSdL4L3bOTauNs6zWKrINSum9p\/fcJ0\/Oy3OKsWKcCYV5jhkqxsi8qcaZ9JzMDCceFWMZS0tPmnIOLLOyHmd4f3t2RNcyF5uKmiOqhZZhcKCkLDxpwhErr6Un4gzLigLHS+Pon24l1Wm5oJPfLSnc4kbF8DjHUCe+r7wpK1ouA8d1LQfwOI5FX7iYKOiwIZOnqpwnPriXCtgo2gAwE30BQLMFE\/0Txf\/2ryHKCziJZEgC3wMZ3D9BhsBHIz2QIf5NZGAc0ygmFkTERRiPjnFccgzJwK3nFkZrkuMEUaLRSqxWHFlPVC2TJe0wDImc1M6O9l+6BJ4YppH9hyzsM\/CC8Cc6sjBoufMsBP4w71pcWONGjuSBrKyWg5qAiTyS12gBgvfQJizhLB95P\/aaq9+cSoMWGprHPed0JBKN9hDG0f7COEhgJ7V8VOCTNIEwZii1ra07KXB9UevVttyvlQCp\/fgZmpvRY1iroSKblppXrVmVSQzd2m\/C3V52j49v7efO8DV\/NtzqTnNzMQAx0GsGXFEkkXZi6rXdvK5vZf8rSteK4q0cuKtbXnXJPq11f3NdVcIDqihsRAyNRWkTojKnSNNwMJKpn0qQcMtf7HrdXdh3P53ZJ5ve\/usAwf34vLPsdT4s2fWSfVxCxN93zxc+3hfWTm3R8Qpv2BerJ06tYjfK3uHnZnnXO4LP3n09wc3b+PnOG7vx3nu35x2suUu7zln94WJ1y2vu+rZTeustNpz1natAB\/H6eozqQVyVcDaq9mnFLVWcjW1npe7UDgNPdF2\/wgYzpVOl0glB4EVpZLQthDvlTtBC5U6SDyVFtt\/ihKguJzcobKpCUgFVHrxyEuxXdLmZmXwF6HGwC0XZMMLO4sQr8VSWwwWZZzK6JIYJ+4JANbiFEh5nQZYupwxCjJlLs65Od1izqpxWYR6IsBK6nzYMmIgvlpkCoUvWF5eKoaPcbSklPEJn7bShPIZxGyw42KY0ogBKHgYCf7D2H5yK3ikjPU9\/wJHCDEzfiV8AAAD\/\/wMAUEsDBBQABgAIAAAAIQADwd4rjwEAAC0EAAASAAAAd29yZC9mb290bm90ZXMueG1stFNba8IwFH4f7D+UvGtiYReKVRjOZ9nlB2RpqmFNTkhSO\/\/9ThvjLorIYC8NOZfvknM6nX\/oJttK5xWYkkzGjGTSCKiUWZfk9WU5uieZD9xUvAEjS7KTnsxn11fTrqgBgoEgfYYYxhdbTG9CsAWlXmyk5n4MVhpM1uA0D3h1a6q5e2\/tSIC2PKg31aiwozljt2QPAyVpnSn2ECOthAMPdehbCqhrJeT+SB3uEt7YuQDRamnCwEidbFADGL9R1ic0\/Vc0tLhJINtzJra6SXWdvYStcrzDgegmyu7AVdaBkN5jdBGTB8QJO8e9f8Ae4tBxiYSfnEmJ5socYPr1+DX\/w\/DGODwauWkP9WUE32L2bZmyrgg7i0heWu54AEcwpKqSjCZDocUrbmv1VBLGHhd3Ocv7iiG0kDVvm3CcWfWh\/OHmdplHkJXrSb3lAl8Q23kdJK4RI3Q2pV1hYz4WJSExhbG+YPimP+CkAQEmKNMOC\/acMJIZFmUk4ceKn\/7Fy0lN53yh1WTSzz4BAAD\/\/wMAUEsDBBQABgAIAAAAIQBm1FFmjgEAACcEAAARAAAAd29yZC9lbmRub3Rlcy54bWy0U91KwzAUvhd8h5L7LVnBKWWdINNrmfoAMU1dsMkJSbq6t\/e0aTZ0YwzBm4acn+8n53Rx\/6WbbCudV2BKMpsykkkjoFLmoyRvr0+TO5L5wE3FGzCyJDvpyf3y+mrRFdJUBoL0GUIYX2wxuwnBFpR6sZGa+ylYaTBZg9M84NV9UM3dZ2snArTlQb2rRoUdzRmbkxEGStI6U4wQE62EAw916FsKqGsl5HikDncJb+xcgWi1NGFgpE42qAGM3yjrE5r+Kxpa3CSQ7TkTW92kus5ewlY53uE8dBNld+Aq60BI7zG6isk94oyd4x4fsIfYd1wi4SdnUqK5MnuYfjt+zX8\/vCkOj0Zu2kMdjOBbLA+7lHVF2FkE8tJyxwM4giFVlWQyG+osXnFXq3VJGHtc3eYs7yuG0ErWvG3Ccea5D+UPN\/OnPII8u57TWy7wAbGd10HiFjFClwvaFTbmY1ESElMY6wuG77j\/p+QLME"
oridoc_5 = "GZdtiul4SQrLAoIsk+1rv+FycnNZ1xhT7TH778BgAA\/\/8DAFBLAwQUAAYACAAAACEAxxxtFJwGAABRGwAAFQAAAHdvcmQvdGhlbWUvdGhlbWUxLnhtbOxZTW8bRRi+I\/EfRntvYyd2Gkd1qtixG2jTRrFb1ON4Pd6denZnNTNO6htqj0hIiIJ6oBLiwgEBlVoJJMqvSSkqRepf4J2Z3fVOvCZJG0EF9SHxzj7v98e8M7546U7E0D4RkvK46VXPVzxEYp8PaRw0vRv97rk1D0mF4yFmPCZNb0qkd2nj\/fcu4nUVkoggoI\/lOm56oVLJ+tKS9GEZy\/M8ITG8G3ERYQWPIlgaCnwAfCO2tFyprC5FmMYeinEEbK+PRtQn6NnPv7z45oG3kXHvMBARK6kXfCZ6mjdxSAx2OK5qhJzKNhNoH7OmB4KG\/KBP7igPMSwVvGh6FfPxljYuLuH1lIipBbQFuq75pHQpwXC8bGSKYJALrXZrjQtbOX8DYGoe1+l02p1qzs8AsO+DpVaXIs9ad63ayngWQPbrPO92pV6pufgC\/5U5nRutVqveSHWxTA3Ifq3N4dcqq7XNZQdvQBZfn8PXWpvt9qqDNyCLX53Ddy80Vmsu3oBCRuPxHFoHtNtNueeQEWfbpfA1gK9VUvgMBdmQZ5cWMeKxWpRrEb7NRRcAGsiwojFS04SMsA9p3MbRQFCsBeB1ggtv7JIv55a0LCR9QRPV9D5MMJTEjN+rp9+\/evoYHd59cnj3p8N79w7v\/mgZOVTbOA6KVC+\/\/ezPhx+jPx5\/\/fL+F+V4WcT\/9sMnz379vBwI5TNT5\/mXj35\/8uj5g09ffHe\/BL4p8KAI79OISHSNHKA9HoFhxiuu5mQgTkfRDzEtUmzGgcQx1lJK+HdU6KCvTTFLo+Po0SKuB28KaB9lwMuT247CvVBMFC2RfCWMHOAO56zFRakXrmhZBTf3J3FQLlxMirg9jPfLZLdx7MS3M0mgb2Zp6RjeDomj5i7DscIBiYlC+h0fE1Ji3S1KHb\/uUF9wyUcK3aKohWmpS\/p04GTTjGibRhCXaZnNEG\/HNzs3UYuzMqu3yL6LhKrArET5PmGOGy\/jicJRGcs+jljR4VexCsuU7E2FX8R1pIJIB4Rx1BkSKctorguwtxD0Kxg6VmnYd9g0cpFC0XEZz6uY8yJyi4\/bIY6SMmyPxmER+4EcQ4pitMtVGXyHuxWinyEOOF4Y7puUOOE+vhvcoIGj0ixB9JuJ0LGEVu104IjGf9eOGYV+bHPg7NoxNMDnXz0syay3tRFvwp5UVgnbR9rvItzRptvmYkjf\/p67hSfxLoE0n9943rXcdy3X+8+33EX1fNJGO+ut0Hb13GCHYjMiRwsn5BFlrKemjFyVZkiWsE8Mu7Co6czxkOQnpiSEr2lfd3CBwIYGCa4+oirshTiBAbvqaSaBTFkHEiVcwsHOLJfy1ngY0pU9Ftb1gcH2A4nVDh\/a5RW9nJ0LcjZmtwnM4TMTtKIZnFTYyoWUKZj9OsKqWqkTS6sa1Uyrc6TlJkMM502DxdybMIAgGFvAy6twQNei4WCCGRlqv9u9NwuLicJZhkiGeEjSGGm752NUNUHKcsXcBEDulMRIH\/KO8VpBWkOzfQNpJwlSUVxtgbgsem8SpSyDZ1HSdXukHFlcLE4Wo4Om16gv1z3k46TpjeBMC1+jBKIu9cyHWQA3Q74SNu2PLWZT5bNoNjLD3CKowjWF9fucwU4fSIRUW1iGNjXMqzQFWKwlWf2X6+DWszLAZvpraLGyBsnwr2kBfnRDS0Yj4qtisAsr2nf2MW2lfKKI6IXDAzRgE7GHIfw6VcGeIZVwNWE6gn6AezTtbfPKbc5p0RVvrwzOrmOWhDhtt7pEs0q2cFPHuQ7mqaAe2FaquzHu9KaYkj8jU4pp\/D8zRe8ncFOwMtQR8OEeV2Ck67XpcaFCDl0oCanfFTA4mN4B2QJ3sfAakgpuk81\/Qfb1f1tzlocpazjwqT0aIEFhP1KhIGQX2pLJvmOYVdO9y7JkKSOTUQV1ZWLVHpB9wvq6B67qvd1DIaS66SZpGzC4o\/nnPqcVNAj0kFOsN6eH5HuvrYF\/evKxxQxGuX3YDDSZ\/3MVS3ZVS2\/Is723aIh+MRuzallVgLDCVtBIy\/41VTjlVms71pzFy\/VMOYjivMWwmA9ECdz3IP0H9j8qfEZMGusNtc\/3oLci+KFBM4O0gaw+ZwcPpBukXRzA4GQXbTJpVta16eikvZZt1mc86eZyjzh"
oridoc_6 = "ba3aSeJ\/S2flw5opzavEsnZ162PG1XVvoaojs0RKFpVF2kDGBMb9pFX914oPbEOgtuN+fMCVNMsFvSgLD6NkzdQDFbyUa0o2\/AAAA\/\/8DAFBLAwQUAAYACAAAACEA89WsXkAEAABTCwAAEQAAAHdvcmQvc2V0dGluZ3MueG1snFbbjts2EH0v0H8w9FyvSZGybCHewNYlm2I3LerkA2iJtoWVRIGk7fV+fYeSGK23TBD0SeScmTMXUpz58PGlriZnLlUpmpWH75A34U0uirI5rLxvX7PpwpsozZqCVaLhK+\/Klffx\/vffPlwixbUGNTUBikZFYuWdZBOp\/MhrpqZ1mUuhxF5Pc1FHYr8vcz58vMFCrryj1m00mw1Gd6LlDbDthayZVndCHma9ZSLyU80bPfMRms8kr5iGgNWxbJVlq\/8vG7g6WpLzz5I415XVu2D0M80h3YuQxXeLXwnPGLRS5FwpqGxd9enWrGwsjap+haev52O5k0xe35Dcw7G9ClFPLlHLZQ4FhTNHyJsZYAfO4SIk4ovQ25OU4tQUD5yB7IdwJoQeYAhb7LeaaQ7kquVV1V2hvOKs6fkLvmenSn9lu60WLWidGSQT+oP7QrILmHySZfEgZPkqGs2qbctyEFpljK1yqdqKXUfFZLRO4TpfrYXf+86PTLIcYh0IY2CXorJahck5FnUrofK9xR5SayC7v6Wpjd2BQVmsvCm+VRrEXXCzUbu35U0xEg2bdzy3UktzYwh\/Ucu0ieWkeJY+sqs4aTgYcDdC8BsXyuiYxT+QgU0QoYTgJBiqZ9ARQWGA02Wf0DtkgcgmdCJxQLLUhWDq443TD56jdUKdNptwQYaS3kaAY7xMFi4bH2O6dEbtb4J5Npz7LZufBGt3DYhPNpS4\/JDAx8QZNVlSkjirQzZ+GLjZEhK686EoyNaZKwLqzzFxslESLNYbpw0Naeo8BbrwKXJWhyYILZwRBNQnbmSeEYLXrghCElB3dRYoQLEztsUmDP25i20ZUxQnTiQJE7efZRqg1HlHN6nvJ04kpgFgLj+J79PAeRN\/\/Gclc7SMnX4AyZaB00+I\/dh539I5CmNnrdMEpcTpJ03gfXXmk2aYpl1F4QUxvwm8G3VkeqF5tfpVBq\/kpO7f6ZjVO1myyZPplvDu1NFOPm\/KxuI7Dl2bv0W2p50Fp9MeUDWrqgxeYgtAo+yRAh70hO874uqJycPI3F2VOpJOKTSVP7+zmYbG5SfoXG3PepGs\/dwUILYOMaUDX9nox7K2cnXaba1VA03zDXRqir\/O0hDOxgJdIg1zDjcVemRjg+LN9NvWg7eVM6XXqmQr7\/U4jb8Ya3ioK7k14xF\/Ym3bt7XdAa+8qjwcNTZmGnYFk8\/dZnfwB8zvMNgZrNuw3CQL2sPCKPRL0BoWo4xYGRll1MroKAusLBhlcyubG9nxCoMDtPZnGEPs0sj3oqrEhRcPVrjy\/iPqi6COrOVw1GYWgDsnok4wDAdqco74C0wlvCg1TJ5tWdTsBYYUeGa6n2JQh94P7e9G2VAZ7fZGOimYhkPomsvsxrhrne+CuUQFz0u4pNtrvRvHg7s+8qpUestbmCS0kJBzN7\/80V2McRq+\/xcAAP\/\/AwBQSwMEFAAGAAgAAAAhAErYipK7AAAABAEAABQAAAB3b3JkL3dlYlNldHRpbmdzLnhtbIzOwWrDMAzG8Xth7xB0X531MEpIUiijL9D1AVxHaQyxZCRt3vb0NWyX3XoUn\/jx7w9faW0+UTQyDfCybaFBCjxFug1weT8976FR8zT5lQkH+EaFw\/i06UtX8HpGs\/qpTVVIOxlgMcudcxoWTF63nJHqNrMkb\/WUm+N5jgHfOHwkJHO7tn11gqu3WqBLzAp\/WnlEKyxTFg6oWkPS+uslHwnG2sjZYoo\/eGI5ChdFcWPv\/rWPdwAAAP\/\/AwBQSwMEFAAGAAgAAAAhAL9gU\/aCAQAA8gIAABEACAFkb2NQcm9wcy9jb3JlLnhtbCCiBAEooAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHySTU\/DMAyG70j8hyr3LskmMai6Ij7EiUlIDIG4hcRsYU0aJYZu\/5603boVELc4fv3YfpP8cmPK5At80JWdET5iJAErK6XtckaeFnfpOUkCCqtEWVmYkS0EclmcnuTSZbLy8OArBx41hCSS"
oridoc_7 = "bMikm5EVossoDXIFRoRRVNiYfK+8ERhDv6ROyLVYAh0zdkYNoFACBW2AqeuJZIdUske6T1+2ACUplGDAYqB8xOlBi+BN+LOgzRwpjcatizvtxj1mK9kle\/Um6F5Y1\/WonrRjxPk5fZnfP7arpto2XkkgRa5khhpLKHJ6OMZT+Hz7AInddR\/EhPQgsPLFlTLa6oC+idrifabxfA3buvIqxPpBFAEKgvTaYXzJjj64iOpSBJzHp33XoK63Pxv9FjT9PHzp5m8UfNp27OO4YOtnNzeoJDqUdX7uM8+Tm9vFHSmiSecpu0g5X\/BpNmYZY6\/NYoP6xrHuwuxG\/JfIL1I2SdnZgk0zNh4S94DOo+EvLb4BAAD\/\/wMAUEsDBBQABgAIAAAAIQDyvb1m7ggAAGJDAAAPAAAAd29yZC9zdHlsZXMueG1s1FvNktvGEb67Ku+Awl1e\/uxyJZUp1+7KG6lKlmVx1z4PgeESFoihAVDS6mwfcsw1ySUvkJx8ciVvk4r1FunpGQxBgCC6CShVPnExmOmve7r76yF3+osv369i761Ms0glU3\/4+cD3ZBKoMErupv7tzfWDh76X5SIJRawSOfXvZeZ\/+eQPn33x7nGW38cy80BAkj1Op\/4yz9ePT06yYClXIvtcrWUC7xYqXYkcHtO7E7VYRIF8qoLNSib5yWgwmJykMhY5gGfLaJ35Vto7irR3Kg3XqQpkloG2q9jIW4ko8Z+AeqEKnsqF2MR5ph\/TV6l9tE\/4ca2SPPPePRZZEEU3oDiYuIoSlT67SLLIhzdSZPlFFomp\/59\/\/+O3f\/3z419\/\/vjrn\/WbpZ6yd02Q5SVRl1EY+ScaLvsAy96KeOqPRsXIlYbfGYtFcleMyeTB7WxXjQ\/LB1cv9dAc5E59kT6YXWhhJ2hj8Vmydb1jOTyhKmsRwK6BGLHIJXgPnKGFxpH28mjkHl5vYhgQ+Qu9ERYHZQBeWTI8VnYc\/Apenpkogbdy8UIFb2Q4y+HF1EcEGLx9\/iqNVBrl91P\/0SOtAwzO5Cp6FoWh1EFpx26TZRTK75cyuc1kuB3\/9hpDzEoM1CbJwYLJOUZBnIVfvQ\/kWocYiE6E9vBLvSDWYrMSDiq0ibbamIEKKg7+WEAOjRv3oiyl0Gnkof4HgdDqTWegkbaobADKZek67i7itLuIs+4iJt1FnHcXAeTZ1SMmNkpRSXdqrgITfOWYGD86ELJ6RS2KWlfUgqZ1RS1GWlfUQqJ1RS0CWlfUHN66oubf1hU1dx5cEQgkrmoUjXE3SIl9E+Wx1OsPEtCwI9XZauO9Eqm4S8V66enCWlX7EFnONvOcpirS6fFkOctTldy17ggUaJ26R3PyV6v1UmQRnGhatt5U2uOBbsQ8lt4f0yhshTozwVezCc8me0vYq1gEcqniUKbejXxvPMpY\/1J5M3PQaFWuo1tfRHfL3JstseS2gk0a4r15J4z8FxGcgdo8OmkwpU04yYeThrhsFv61DKPNqtgawmlkYvic4eYKBKp4kG8mp3oX60HfaoV2AMUEUy74JqB8gv6muPDlax9T9Del6Ej5BP1N4TpSPsbHYf+ymeapSN94pPQ6Z+fulYpVutjERQ60ZvA5O4MdBM0EdhI7+SSSOGdn8A59ehdBAN\/cKHHK9sWWRxkobHcYFEw2ui1sp1Rob8iwiO2gCtaIgdWNaxlAbNJ9Ld9G+ocnbjFAlnZnzdZ0HjfsAJQg0hn6243K28\/QowbOo6I8T+Dnkkx6NLRxQ+ZR0Ww8mXrH8HG3wscA6lYBGUDdSiEDqCE+ms88ribSQboXRwYWm5ZdFcOwIzPzOZuZHRCvBPRUNwnnr4bsbY6Fet0koLAdVK+bBBS2dyq1zNVNAlZvdZOA1VA1mn1U5lSOUey6WQZyJwGCRf2QNwGoH\/ImAPVD3gSg7uTdDtIfeROw2NzgOLVM3gQgnML5qu+AyuRNAGJzg2E7+5tRUfdQyuEvtz2QNwGF7aA6eRNQ2N5pIm8CFk7hREIFy1EdAasf8iYA9UPeBKB+yJsA1A95E4D6IW8CUHfybgfpj7wJWGxucJxaJm8CEJseHFCZvAlAOIXDDXvJG7P+k5M3AYXtoDp5E1DY3qkQqjukErDYDqpgOfImYOEUTjBYLAxujlH9kDfBon7ImwDUD3kTgPohbwJQd\/JuB+mPvAlYbG5wnFombwIQmx4cUJm8CUBsbthL3piMn5y8CShsB9XJm4DC9k6FUB3PEbDYDqpgOfImYGG8dCZvAhBOORaIY1E\/5E2wqB\/yJgD1Q94EoO7k3Q7SH3kTsNjc4Di1TN4EIDY9OKAyeROA2Nywl7wxRz45eRNQ2A6qkzcBhe2dCqE68iZgsR1UwXJUR8Dqh7wJQBiYncmbAIRTjgDCLOK4qR\/yJljUD3kTgLqTdztIf+RNwGJzg+PUMnkTgNj04IDK5E0AYnODvmcL90XJ11OHDUFAvWdQ3GogA44anEQFtAa+lguZQieTbL8d0hGwsJC"
oridoc_8 = "B2BAeVBMvlXrj0S52jxsChAwVzeNI4ZXue7ylU2pEGJ8f6CS4+ebKe2YaYGrrMKR2b95A91C5XQg7lHTjEOiZ36+hZWdd3CzX0qBBSPd12RYg7EN7Dg1BAjt+dIsPzMGWKtvog\/+ytYD4N7S7hcWcwWA8Gl+ejo0xtj1KhD9ssvy1vlT8PNlONXOyRKxvFGaqxRnYF66pyrZRneK\/ivSDbaPa5EpPNb1T2IFm2rHSnUa0qX8jlmoltK3YZeYGzFroZUMZaHl9r4IlbFYAXV2H9mpQ26yGS\/y4YdsOkmLb7GX+7ZHPzNu5Umq0bdAy1xfXD2k4rGlo3OnhlXez43W9oIUMNWlTzN39wtn5PDaOgD+Mw6EFEZ1nwi98L4xYeH8l4\/hrAR6A2FRr2I+GqbFc5ObtcIA1uyJqrvJcrZrXp3ilHcXvEwAxVFbGPB4OjGSzmssUetIObftoz7abm7nGw44Bikig7jho2BYK21Qe17QoNTqgInMBXYDf6KY+THVhA7IeEdD2gAt2k\/50cHZ9cW3eNPVEuuyFfsL2VObE0CX0rkLT7TaG0Abdx2q7dT5MffPDG1BK0SwZ6HvMQHOWRIAyTYQdtdZF31Gri9g8anEEfbOhfFZ4jmu1Wf7dcctNmpS3\/\/ec0DtVcZs8p7Xk0b2oUA\/2Jo4ZhSL1ptjSKyggZrSeTdRsh27knSI7ujybXNuuZ5tv68sQWfRQKJozsEkCPKhVkgD8WYiBgmISSswLQ\/Q1dlMG1yqDjBqe2TIPc4s5GMqaEHHKw\/Fgok3XcWLl\/RAUU60489oagbUYmM21dg8fmq3LPmxbu80YyORU7gBOIGo108eg6kkHHaTJo3zY+fj3X\/77tz95W+dVGdKeUsqeFqdMPzc71W4E4yTT1641ZMFZLQsWCi5ys7LAbtknTYMizkox2UPc6sSwZ0vz8f+P0PoRE0L0t5\/+wgzRs99hiMLuIx1nT\/4HAAD\/\/wMAUEsDBBQABgAIAAAAIQBsI5j7PQIAAEIHAAASAAAAd29yZC9mb250VGFibGUueG1stJRNbtswEIX3BXoHgftGFG0rihE5SNxomUWTHoCWaYuASAokHTUH6KqrosveIT1AkZymAZpbdEjJCmDXsNUfCiCgGWo0+PjenJ59EGVwy7ThSqYoOsIoYDJXcy6XKXp\/k71JUGAslXNaKslSdMcMOpu8fnVajxdKWhPA99KMdYoKa6txGJq8YIKaI1UxCbmF0oJaeNXLUC0WPGdvVb4STNqQYByHmpXUwr9NwSuD2mr1IdVqpeeVVjkzBpoVZVNPUC7RpO0uqMeSCuh6Sks+09wnKiqVYRHkbmmZIkxwhkewu2eIB25HoauQF1QbZruDuAkvqODl3Tpqam5Mk6i4zYt1\/JZqTmcla1KGLyGxMjOcoksMi2QZaiJRioYQOJ92EQJNNStqzwy6CFwPNObr+CPRia8DEajTfuX7DJv72SLx9Hj\/8+Hb89ePz98\/78BxATgcBofD77\/FkcT\/BkfiuibJ8QsOkuBsMB2RNtLhiOI9OIBj1BPHDRfMBFesDt4pQRvlbAuE4BiIjICHE8qgl0C0r+s"
oridoc_9 = "F1UMg5LyTA1zsFBAdJ8O1HDoi+GQPEQekLxFaQMc7pRF7jzgUThz\/2SkRKONyE0SMRxeb0iD7QET9QTzdf\/rx8MWDoKW9gjmy9vY1F9cr2Zp+a5pEIBYMIoFfNk8P+9CVVW3dw4aJMw+sQQsEtEKSJHOhTUSHuAd7hR0+TKZUwFTdJRbnlsY1zj39xPJnrtkeq3jYyefFNWs2fzNW2\/lqJr8AAAD\/\/wMAUEsDBBQABgAIAAAAIQAaq+YedwEAAMYCAAAQAAgBZG9jUHJvcHMvYXBwLnhtbCCiBAEooAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJxSy07DMBC8I\/EPUe7U6UMFoY0r1Apx4CU10LPlbBILx7ZsU7V\/z4bQNIgbPu3M2uPZsWF1aHWyRx+UNXk6nWRpgkbaUpk6T9+K+6ubNAlRmFJoazBPjxjSFb+8gFdvHfqoMCQkYUKeNjG6W8aCbLAVYUJtQ53K+lZEgr5mtqqUxI2Vny2ayGZZtmR4iGhKLK\/cIJj2irf7+F\/R0srOX3gvjo4McyiwdVpE5M+dHQ1sIKCwUehCtciX18QPCF5FjYFPgfUF7KwvA19mwPoK1o3wQkYKj88XC2AjDHfOaSVFpFj5k5LeBlvF5OU7gKQ7D2y8BSiULcpPr+KR0w1jCI\/KkJEZsL4gY17UXrjmx92AYCuFxjVNziuhAwI7E7C2rRPmyMnnqSK9j\/DmCrvpovk58pscDblTsdk6IcnLIpuPxx11YEuhYEn+T3pnAh7oNbzuLqWoTI3lac\/fRhfge\/8t+XQ2yWh9J3bi6FWG\/8K\/AAAA\/\/8DAFBLAQItABQABgAIAAAAIQBvGmuQfgEAACgGAAATAAAAAAAAAAAAAAAAAAAAAABbQ29udGVudF9UeXBlc10ueG1sUEsBAi0AFAAGAAgAAAAhAB6RGrfzAAAATgIAAAsAAAAAAAAAAAAAAAAAtwMAAF9yZWxzLy5yZWxzUEsBAi0AFAAGAAgAAAAhABEXoNkUAQAAOQQAABwAAAAAAAAAAAAAAAAA2wYAAHdvcmQvX3JlbHMvZG9jdW1lbnQueG1sLnJlbHNQSwECLQAUAAYACAAAACEATorJOTUNAAAobwAAEQAAAAAAAAAAAAAAAAAxCQAAd29yZC9kb2N1bWVudC54bWxQSwECLQAUAAYACAAAACEAA8HeK48BAAAtBAAAEgAAAAAAAAAAAAAAAACVFgAAd29yZC9mb290bm90ZXMueG1sUEsBAi0AFAAGAAgAAAAhAGbUUWaOAQAAJwQAABEAAAAAAAAAAAAAAAAAVBgAAHdvcmQvZW5kbm90ZXMueG1sUEsBAi0AFAAGAAgAAAAhAMccbRScBgAAURsAABUAAAAAAAAAAAAAAAAAERoAAHdvcmQvdGhlbWUvdGhlbWUxLnhtbFBLAQItABQABgAIAAAAIQDz1axeQAQAAFMLAAARAAAAAAAAAAAAAAAAAOAgAAB3b3JkL3NldHRpbmdzLnhtbFBLAQItABQABgAIAAAAIQBK2IqSuwAAAAQBAAAUAAAAAAAAAAAAAAAAAE8lAAB3b3JkL3dlYlNldHRpbmdzLnhtbFBLAQItABQABgAIAAAAIQC\/YFP2ggEAAPICAAARAAAAAAAAAAAAAAAAADwmAABkb2NQcm9wcy9jb3JlLnhtbFBLAQItABQABgAIAAAAIQDyvb1m7ggAAGJDAAAPAAAAAAAAAAAAAAAAAPUoAAB3b3JkL3N0eWxlcy54bWxQSwECLQAUAAYACAAAACEAbCOY+z0CAABCBwAAEgAAAAAAAAAAAAAAAAAQMgAAd29yZC9mb250VGFibGUueG1sUEsBAi0AFAAGAAgAAAAhABqr5h53AQAAxgIAABAAAAAAAAAAAAAAAAAAfTQAAGRvY1Byb3BzL2FwcC54bWxQSwUGAAAAAA0ADQBAAwAAKjcAAAAA"

# 原始简历的
original_content1 = "ZnJvbV9qc29uX2VuY29kZV9yZXN1bHQ6eyJzdGF0ZSI6MSwibWVzc2FnZSI6IuaTjeS9nOaIkOWKnyIsImNvbnRlbnQiOnsiZGF0YSI6eyJwb3NpdGlvbk5hbWUiOiLnvZHnu5zlt6XnqIvluIgiLCJkZWxpdmVyVGltZSI6IjIwMTktMDItMjUgMTk6NDciLCJwb3NpdGlvbklkIjo0NDE2NjA2LCJoYXZlSW50ZXJ2aWV3IjpmYWxzZSwicmVzdW1lVmVyc2lvbiI6IlY0IiwieXVuc3RhdHVzIjoiIiwicmVzdW1lVm8iOnsiaWQiOiI1YzZiZTUwMjE4MjNjZTMzN2JjYjlhOTYiLCJzZXgiOiLnlLciLCJiaXJ0aGRheSI6IjE5ODkuMTAiLCJiaXJ0aFllYXIiOjE5ODksImJpcnRoTW9udGgiOiIxMCIsImJpcnRoRGF0ZSI6IjEiLCJhZ2VOdW0iOjMwLCJ3b3JrWWVhciI6IjblubQiLCJwaG9uZSI6IjE1ODIxNzc1Mjc4IiwiZW1haWwiOiJkYW5tZHJAMTYzLmNvbSIsInN0YXR1cyI6IuaIkeebruWJjeW3suemu+iBjO+8jOWPr+W\/q+mAn+WIsOWylyIsIm15UmVtYXJrIjoiPHVsPiBcbiA8bGk+PHA+Jm5ic3A75pys5Lq65oSP5ZCR55S15ZWG5oiW6auY5bm25Y+R77yM6LSj5Lu75b+D6Z2e5bi45by677yM6ICQ5Yqb5oyB5LmF77yM54Ot54ix5oqA5pyv77yM55qu5a6e44CC5pys5Lq656ym5ZCI56iL5bqP5ZGY54m55b6B5YaF5pWb44CB54G15rS744CB5omn552A44CC54Ot6KG35LqO5oqA5pyv77yM5bSH5bCa56eR5oqA5pS55Y+Y5LiW55WM44CCJm5ic3A7PGJyIC8+PC9wPjwvbGk+XG48L3VsPiIsInJlc3VtZU5hbWUiOiLlvKDmmI7nmoTnroDljoYiLCJuYW1lIjoi5byg5piOIiwibmFtZURlcyI6IiIsImNyZWF0ZVRpbWUiOiIyMDE5MDIxOVQxOTAzNDArMDgwMCIsInVwZGF0ZVRpbWUiOiIyMDE5MDIxOVQxOTA5MjgrMDgwMCIsInJlZnJlc2hUaW1lIjoiMjAxOS0wMi0xOSAxOTowOSIsInBlcmZlY3QiOiIxMTExMDEwMTExMDAwMDAxMTExMDAwMDAxMTEwMDAxMDExMDAxMTExMTAxMSIsImhlYWRQaWMiOiJjb21tb24vaW1hZ2UvcGMvZGVmYXVsdF9ib3lfaGVhZHBpYzMucG5nIiwidXNlcklkIjo0OTA4MTQ1LCJoaWdoZXN0RWR1Y2F0aW9uIjoi5pys56eRIiwib25lV29yZCI6IuWBmuS6i+iupOecn+OAgei0n+i0o++8jOazqOmHjeWboumYn+WQiOS9nOOAgiIsImxpdmVDaXR5Ijoi5LiK5rW3IiwidXNlcklkZW50aXR5IjoyLCJyZXN1bWVJZCI6Mzk4NjQ2NSwicmVzdW1lU2NvcmUiOi0xLCJyZXN1bWVLZXkiOiIiLCJjb21wYW55TmFtZSI6IuS4nOiOnue+juWunOS9syIsIndvcmtFeHBlcmllbmNlcyI6W3siY29tcGFueU5hbWUiOiLoh7PlloTnvZHnu5zogqHku73mnInpmZDlhazlj7giLCJwb3NpdGlvbk5hbWUiOiJQSFAiLCJzdGFydERhdGUiOiIyMDEzLjAzIiwiZW5kRGF0ZSI6IjIwMTYuMDQiLCJjcmVhdGVUaW1lIj"
original_content2 = "oiMjAxNjA0MjVUMDEzNzA2KzA4MDAiLCJ3b3JrQ29udGVudCI6IjxwPiZuYnNwO+S\/oeaJmOWfuue6v+eJiDQuMCDliY3nq6\/lvIDlj5Hlt6XnqIvluIgg5oGS55Sf55S15a2Q6IKh5Lu95pyJ6ZmQ5YWs5Y+4IOS4u+imgei0n+i0o+S7u+WKoe+8miDlj4LkuI7kv6HmiZjkuJrliqHnmoTliLblrprvvIzmlbTlkIjkvJjnp4Dkv6HmiZjlhazlj7jova\/ku7bnmoTnibnngrnvvJsg5Yi25a6a5Z+657q\/54mI5byA5Y+R55qE5Lu75Yqh6KeE5YiS77yM5bm25Y+C5LiO5byA5Y+R77ybIOWNj+iwg+a1i+ivlee8luWGmea1i+ivleeUqOS+i++8myDmioDmnK\/vvJpsaWdodCArIHZ1ZSArIHdlZXgg5pS26I6377yaIOWNj+iwg+ayn+mAmuihqOi+vuiDveWKm+W+l+WIsOS6huW+iOWkp+eahOaPkOmrmO+8myDov5vkuIDmraXmjozmj6Hkv6HmiZjkuJrliqHmqKHlnZfvvJrnlLXlrZDlkIjlkIzvvIzkv6Hmga\/miqvpnLLvvIzlrp7lkI3orqTor4HnrYnvvJsg54af5oKJ5L+h5omY55qE5Lqk5piT5rWB56iL77ya6K+35rGC4oCUJmd0O1RBJmFncmF2ZTvpk7bogZTmiaPmrL7igJQmZ3Q76L+U5ZueVEEmbmJzcDs8YnIgLz48L3A+IiwiZGVwYXJ0bWVudCI6IueglOWPkSIsInNraWxsTGFiZWxzIjpbIuWQjuerryIsIuacjeWKoeWZqOerryJdfV0sImxhdGVzdFdvcmtFeHBlcmllbmNlIjp7ImNvbXBhbnlOYW1lIjoi6Iez5ZaE572R57uc6IKh5Lu95pyJ6ZmQ5YWs5Y+4IiwicG9zaXRpb25OYW1lIjoiUEhQIiwic3RhcnREYXRlIjoiMjAxMy4wMyIsImVuZERhdGUiOiIyMDE2LjA0IiwiY3JlYXRlVGltZSI6IjIwMTYwNDI1VDAxMzcwNiswODAwIiwid29ya0NvbnRlbnQiOiI8cD4mbmJzcDvkv6HmiZjln7rnur\/niYg0LjAg5YmN56uv5byA5Y+R5bel56iL5biIIOaBkueUn+eUteWtkOiCoeS7veaciemZkOWFrOWPuCDkuLvopoHotJ\/otKPku7vliqHvvJog5Y+C5LiO5L+h5omY5Lia5Yqh55qE5Yi25a6a77yM5pW05ZCI5LyY56eA5L+h5omY5YWs5Y+46L2v5Lu255qE54m554K577ybIOWItuWumuWfuue6v+eJiOW8gOWPkeeahOS7u+WKoeinhOWIku+8jOW5tuWPguS4juW8gOWPke+8myDljY\/osIPmtYvor5XnvJblhpnmtYvor5XnlKjkvovvvJsg5oqA5pyv77yabGlnaHQgKyB2dWUgKyB3ZWV4IOaUtuiOt++8miDljY\/osIPmsp\/pgJrooajovr7og73lipvlvpfliLDkuoblvojlpKfnmoTmj5Dpq5jvvJsg6L+b5LiA5q2l5o6M5o+h5L+h5omY5Lia5Yqh5qih5Z2X77ya55S15a2Q5ZCI5ZCM77yM5L+h5oGv5oqr6Zyy77yM5a6e5ZCN6K6k6K+B562J77ybIOeGn+aCieS\/oeaJmOeahOS6pOaYk+a1geeoi++8muivt+axguKAlCZndDtUQSZhZ3JhdmU76ZO26IGU5omj5qy+4oCUJmd0O+i\/lOWbnlRBJm5ic3A7PGJyIC8+PC9wPiIsImRlcGFydG1lbnQiOiLnoJTlj5EiLCJza2lsbExhYmVscyI6WyLlkI7nq68iLCLmnI3liqHlmajnq68iXX0sImVkdWNhdGlvbkV4cGVyaWVuY2VzIjpbeyJzY2hvb2xOYW1lIjoi5Y2X5piM5aSn5a2mIiwiZWR1Y2F0aW9uIjoi5pys56eRIiwicHJvZmVzc2lvbmFsIjoi6K6h566X5py656eR5"
original_content3 = "a2m5LiO5oqA5pyvIiwic3RhcnREYXRlIjoiMjAwNyIsImVuZERhdGUiOiIyMDExIiwic2Nob29sQmFkZ2UiOiJpL2ltYWdlL00wMC9BRC81MS9DZ3AzTzFpMUU3cUFlODZtQUFBdWtBYzhHT1ExNS5qcGVnIiwid2hldGhlckdyYWR1YXRlIjp0cnVlLCJ3aGV0aGVyRnJlc2giOmZhbHNlfV0sImxhdGVzdEVkdWNhdGlvbkV4cGVyaWVuY2UiOnsic2Nob29sTmFtZSI6IuWNl+aYjOWkp+WtpiIsImVkdWNhdGlvbiI6IuacrOenkSIsInByb2Zlc3Npb25hbCI6Iuiuoeeul+acuuenkeWtpuS4juaKgOacryIsInN0YXJ0RGF0ZSI6IjIwMDciLCJlbmREYXRlIjoiMjAxMSIsInNjaG9vbEJhZGdlIjoiaS9pbWFnZS9NMDAvQUQvNTEvQ2dwM08xaTFFN3FBZTg2bUFBQXVrQWM4R09RMTUuanBlZyIsIndoZXRoZXJHcmFkdWF0ZSI6dHJ1ZSwid2hldGhlckZyZXNoIjpmYWxzZX0sImxhdGVzdEVkdUFuZEV4cCI6IlBIUCAmbWlkZG90OyDoh7PlloTnvZHnu5zogqHku73mnInpmZDlhazlj7ggfCDmnKznp5EgJm1pZGRvdDsg5Y2X5piM5aSn5a2mIiwicHJvamVjdEV4cGVyaWVuY2VzIjpbeyJwcm9qZWN0TmFtZSI6Iuezu+e7nyIsInBvc2l0aW9uTmFtZSI6IiIsInN0YXJ0RGF0ZSI6IjIwMTMuMDYiLCJlbmREYXRlIjoiMjAxNi4wMSIsInByb2plY3RSZW1hcmsiOiI8cD7pobnnm67ns7vnu588L3A+IiwiZHV0eVJlbWFyayI6IjxwPueLrOeri+WujOaIkDwvcD4iLCJyZXN1bWVJZCI6Mzk4NjQ2NSwiY3JlYXRlVGltZSI6IjIwMTkwMjE5VDE5MDkyOCswODAwIiwicHJvamVjdFVybCI6IiIsInByb2plY3ROYW1lQW5kUmVtYXJrIjoi57O757ufIn1dLCJleHBlY3RKb2IiOnsiY2l0eSI6IuS4iua1tyIsInBvc2l0aW9uVHlwZSI6IuWFqOiBjCIsInBvc2l0aW9uTmFtZSI6IlBIUCIsInNhbGFyeXMiOiIxNWstMzBrIiwiYWRkRXhwbGFpbiI6IiIsImFycml2YWxUaW1lIjoiM+S4quaciOS7peS4iiIsInN0YXR1cyI6Iumaj+S+v+eci+eciyJ9LCJleHBlY3RKb2JTdHIiOiLkuIrmtbfvvIzlhajogYzvvIzmnIjolqoxNWstMzBr77yMUEhQIiwic29jaWFsQWNjb3VudHMiOltdLCJ1c2VyRGVmaW5lIjp7InRpdGxlTmFtZSI6IuaKgOacr+a4heWNlSIsInRpdGxlQ29udGVudCI6Ijx1bD5cbiA8bGk+54af5oKJZmFzdGNnaeOAgXBocC1mcG3jgII8L2xpPlxuIDxsaT7nhp\/mgonmlbDmja7lupPov57mjqXmsaDjgIFlcG9sbOOAgWVhY2NlbGVyYXRvcuOAgXBjbnRs44CBcmFiYml0bXHjgIFzaWVnZSjmgKfog73ljovlipvmtYvor5Up44CCPC9saT5cbiA8bGk+54af5oKJbWVtY2FjaGXjgIFyZWRpc++8jHJlZGlz55u45YWz6YWN572u5LyY5YyW77yMcmVkaXPlpIfku73jgII8L2xpPlxuIDxsaT7nhp\/mgolNeXNxbO+8jG15aXNhbeOAgWlubm9kYuW8leaTju+8jOWtmOWCqOi\/h+eoi++8jOS4u+S7juWkh+S7veetieOAgjwvbGk+XG4gPGxpPueGn+aCiVRDUOOAgVVEUOOAgXNvY2tldOOAgjwvbGk+XG4gPGxpPueGn+aCiUxpbnV444CBU2hlbGzjgII8L2xpPlxuIDxsaT7nhp\/mgolweXRob27jgIFub2RlanPjgIFqYXZh44CBYW5kcm9pZOOAgjwvbGk+XG4gPGxpPuS6huino0x1YeOAgjwvbGk+XG48L3VsPiIsImNyZWF0ZVRpbWUiOiIyMDE2MDQyNVQwMTQ4MTQrMDgwMCJ9LCJza2lsbEV2YWx1YXRlcyI6W10sIndvcmtTaG93cyI6W10sImFiaWxpdHlMYWJlbHMiOlsi5Liq5Lq66IO95YqbIiwi5rKf6YCa5Y2P6LCD6IO95YqbIl19LCJvcGVuQ29weSI6ZmFsc2UsImRlbGl2ZXJJZCI6MTA5OTk5OTIwNTM0MDcyOTM0NCwibWFyayI6ZmFsc2UsInN0YXR1cyI6IkFVVE9fRklMVEVSIn0sInJvd3MiOltdfX0="
environment_type = 't'


class tob_rpc():
    def __init__(self):
        pass

    def tob_delivery_inner(self):
        url = '/atsng/rpc'
        api = rpcAPI(environment_type, url)
        # $p = [
        # 'position_name' => '网络工程师', // 职位名称 必填
        # 'city_name' => '', // 城市名称
        # 'sourceJidFrom' => 11, // 投递渠道 必填
        # 'deliveryTime' => false, // 投递时间 必填
        # 'email' => 'baolong.yang@ifchange.com', // 邮箱用户名 必填   baolong.yang@ifchange.com是非白名单    ying.zhang@ifchange.com是白名单用户
        # 'password' => 'abc123', // 邮箱密码 必填
        # 'subject' => '网络工程师：张明的简历（来自拉勾）', // 邮件主题 必填
        # 'originalExt' => 'html', // 简历原件格式 必填
        # 'content' => '', // 简历格式化数据 必填
        # 'original_content' => '', // 简历原件格式 必填
        # 'ifchange_position_ids' => '',//基础数据职位ID，兼容参数    以后可能会没有
        # ];
        api.params = {
            "request": {
                "p": {
                    "position_name": "lp测试职位3",
                    "city_name": "上海",
                    "sourceJid": "",
                    "sourceJidFrom": "1",
                    "deliveryTime": 1551877541,
                    "email": "ying.zhang@ifchange.com",
                    "password": "Zhang2016",
                    "vipname": "",
                    # "ifchange_position_ids":[6836640],
                    "type": 1,
                    "originalExt": "html",
                    "subject": "lp测123sad费",
                    "content": content,
                    # "content":source+contact+basic+work+project+education,
                    "original_content":original_content1+original_content2+original_content3
                    # "original_content": oridoc_1 + oridoc_2 + oridoc_3 + oridoc_4 + oridoc_5 + oridoc_6 + oridoc_7 + oridoc_8 + oridoc_9
                },
                "c": "delivery",
                "m": "emailDelivery"
            },
            "header": {
                "provider": "testing_aide",
                "uid": 1226
            }
        }
        result = api.do_test()


content = "{\"source\":{\"src\":\"1\",\"src_no\":\"5c6bswqe37bcb9a96\"},\"contact\":{\"phone\":\"15999990021\",\"email\":\"lptestingemail21@163.com\"},\"basic\":{\"resume_name\":\"lp\\u90ae\\u4ef6\\u6d4b\\u8bd521\\u7684\\u7b80\\u5386\",\"name\":\"lp\\u90ae\\u4ef6\\u6d4b\\u8bd521\",\"gender\":\"M\",\"work_experience\":\"6\",\"birth\":\"1989\\u5e7410\\u6708\",\"age\":\"30\",\"expect_type\":\"\\u5168\\u804c\",\"address\":\"105\",\"expect_position_name\":\"PHP\",\"current_status\":\"1\",\"updated_at\":\"2019-02-19 19:09:00\",\"expect_city_ids\":\"105\",\"expect_salary_from\":\"15\",\"expect_salary_to\":\"30\"}}"


# source = "{\"source\":{\"src\":\"19\",\"src_no\":\"5c6be5021823ce337bcb9a96\"},"
# contact = "\"contact\":{\"phone\":\"15999990019\",\"email\":\"lptestingemail19@163.com\"},"
# basic = "\"basic\":{\"resume_name\":\"lp\\u90ae\\u4ef6\\u6d4b\\u8bd518\\u7684\\u7b80\\u5386\",\"name\":\"lp\\u90ae\\u4ef6\\u6d4b\\u8bd518\",\"gender\":\"M\",\"work_experience\":\"6\",\"birth\":\"1989\\u5e7410\\u6708\",\"age\":\"30\",\"expect_type\":\"\\u5168\\u804c\",\"expect_city_names\":\"\\u4e0a\\u6d77\",\"address\":\"105\",\"expect_position_name\":\"PHP\",\"current_status\":\"1\",\"updated_at\":\"2019-02-19 19:09:00\",\"self_remark\":\" \\n  \\u672c\\u4eba\\u610f\\u5411\\u7535\\u5546\\u6216\\u9ad8\\u5e76\\u53d1\\uff0c\\u8d23\\u4efb\\u5fc3\\u975e\\u5e38\\u5f3a\\uff0c\\u8010\\u529b\\u6301\\u4e45\\uff0c\\u70ed\\u7231\\u6280\\u672f\\uff0c\\u76ae\\u5b9e\\u3002\\u672c\\u4eba\\u7b26\\u5408\\u7a0b\\u5e8f\\u5458\\u7279\\u5f81\\u5185\\u655b\\u3001\\u7075\\u6d3b\\u3001\\u6267\\u7740\\u3002\\u70ed\\u8877\\u4e8e\\u6280\\u672f\\uff0c\\u5d07\\u5c1a\\u79d1\\u6280\\u6539\\u53d8\\u4e16\\u754c\\u3002 \\n\\n\",\"expect_city_ids\":\"105\",\"expect_salary_from\":\"15\",\"expect_salary_to\":\"30\"},"
# work="\"work\":[{\"corporation_name\":\"\\u81f3\\u5584\\u7f51\\u7edc\\u80a1\\u4efd\\u6709\\u9650\\u516c\\u53f8\",\"position_name\":\"PHP\",\"start_time\":\"2013\\u5e7403\\u6708\",\"end_time\":\"2016\\u5e7404\\u6708\",\"so_far\":\"N\",\"responsibilities\":\"\\u5de5\\u4f5c\\u63cf\\u8ff0\\uff1a\\n&nbsp;\\u4fe1\\u6258\\u57fa\\u7ebf\\u72484.0 \\u524d\\u7aef\\u5f00\\u53d1\\u5de5\\u7a0b\\u5e08 \\u6052\\u751f\\u7535\\u5b50\\u80a1\\u4efd\\u6709\\u9650\\u516c\\u53f8 \\u4e3b\\u8981\\u8d1f\\u8d23\\u4efb\\u52a1\\uff1a \\u53c2\\u4e0e\\u4fe1\\u6258\\u4e1a\\u52a1\\u7684\\u5236\\u5b9a\\uff0c\\u6574\\u5408\\u4f18\\u79c0\\u4fe1\\u6258\\u516c\\u53f8\\u8f6f\\u4ef6\\u7684\\u7279\\u70b9\\uff1b \\u5236\\u5b9a\\u57fa\\u7ebf\\u7248\\u5f00\\u53d1\\u7684\\u4efb\\u52a1\\u89c4\\u5212\\uff0c\\u5e76\\u53c2\\u4e0e\\u5f00\\u53d1\\uff1b \\u534f\\u8c03\\u6d4b\\u8bd5\\u7f16\\u5199\\u6d4b\\u8bd5\\u7528\\u4f8b\\uff1b \\u6280\\u672f\\uff1alight + vue + weex \\u6536\\u83b7\\uff1a \\u534f\\u8c03\\u6c9f\\u901a\\u8868\\u8fbe\\u80fd\\u529b\\u5f97\\u5230\\u4e86\\u5f88\\u5927\\u7684\\u63d0\\u9ad8\\uff1b \\u8fdb\\u4e00\\u6b65\\u638c\\u63e1\\u4fe1\\u6258\\u4e1a\\u52a1\\u6a21\\u5757\\uff1a\\u7535\\u5b50\\u5408\\u540c\\uff0c\\u4fe1\\u606f\\u62ab\\u9732\\uff0c\\u5b9e\\u540d\\u8ba4\\u8bc1\\u7b49\\uff1b \\u719f\\u6089\\u4fe1\\u6258\\u7684\\u4ea4\\u6613\\u6d41\\u7a0b\\uff1a\\u8bf7\\u6c42\\u2014&gt;TA&agrave;\\u94f6\\u8054\\u6263\\u6b3e\\u2014&gt;\\u8fd4\\u56deTA&nbsp;\\n\"}],"
# project="\"project\":[{\"name\":\"\\u7cfb\\u7edf\",\"position_name\":\"\",\"start_time\":\"2013\\u5e7406\\u6708\",\"end_time\":\"2016\\u5e7401\\u6708\",\"so_far\":\"N\",\"describe\":\"\\u9879\\u76ee\\u7cfb\\u7edf\\n\",\"responsibilities\":\"\\u7cfb\\u7edf\"}],"
# education = "\"education\":[{\"school_name\":\"\\u5357\\u660c\\u5927\\u5b66\",\"end_time\":\"2011\\u5e74\",\"so_far\":\"N\",\"degree\":\"1\",\"degree_origin\":\"\\u672c\\u79d1\",\"degree_origin_txt\":\"\\u672c\\u79d1\",\"discipline_name\":\"\\u8ba1\\u7b97\\u673a\\u79d1\\u5b66\\u4e0e\\u6280\\u672f\",\"start_time\":\"2007\\u5e74\"}]}"


class rpcAPI():
    params = {}

    def __init__(self, test_type, api_url, base_url=''):
        self.api_url = api_url
        self.test_type = test_type

        if test_type == 't':
            if base_url == '':
                self.base_url = 'http://testing2.common-ats.rpc'
        else:
            if base_url == '':
                self.base_url = 'http://common-ats.rpc'

    def do_test(self, datatype='json'):
        if datatype != 'json':
            r = requests.post(self.base_url + self.api_url, data=self.params)
        else:
            r = requests.post(self.base_url + self.api_url, json=self.params)
        response = r.text
        print(response)
        return json.loads(response)


if __name__ == "__main__":
    obj = tob_rpc()
    obj.tob_delivery_inner()


