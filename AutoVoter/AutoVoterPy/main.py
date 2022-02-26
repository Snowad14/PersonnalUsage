import requests

s = requests.Session()

hd = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "pseudo": "",
    "capchat": "P0_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiTWRkditPd0w3WDNoT2FCRDROZ2U3VzVnYkNoa3JwYUpRV3RJTGFSS0xXcFFkVnhuaDc3LzZUSERwVUdIRTg0VGlTY2tWS2tvbU4yL0o4QW5zQVg5cUU0VGp1eXpxUTlmTDMrb0NCSXFKQ2JaRFRya3V0djMvdlFLQzY0UTJ0cFlLekV1OXl0VllJQ1pyQ0F6MGkrZ0hvQ2ZyWUNmNnRBZHA2SWpnc2tIWmxZQ2dBUi9kVUt2aTY4bCtocFpqTWpCSm90T01LMTdtVkFYb0NMckFWNkh1NDhoWkgwczVNRFdzdS85UE9YdURiZkI1SmI4TkljcDhuZzJDdHI5V0V4Y01OS2JXcmJZVzVmMmw5WWFaY0FpNG5ON3c0cVZQZnRRak8yQnFNM1JqMzZ2QkFocU0zYWhURFFHY1QxSFY1eGgwc3pGWDVBNjU3WmFMVkEyMm84R0ZWQzFwWjJ3dkUzSVcrOTRIY21ReU1jMlpvN0l2aTd2UFhDaXBQVlBOUjZCNEJFbzl1K2tLZENDdDNzdXd0VnZQbG9yMFZQKzV1RVZhQm9yK2RrUUxnVUtydVJiQzBKSFN0V1FHV1c2MU9aR2grUUJ3OTFXdm5LcnovUDdTOWtjN0w3QzRsSDVpQzcvSGFZcTlyR1JjSjFiZm40c0ZnTWZGdHpua1JhZUhaNTJhY1pUQ2pRMDFyM1ZibTVVRXdMSUtzQmNickdrNUFxdVRpa1ZNNXE5NUVUQXN3NzF0SjdLNDhUNk5mRVVUVHF6RjVTMEl6YlNGWkVaZXJjTU9Tdzd4OFBtSXVuVmk2UUVEaTU5Q2ZHVUdudzk0eHRZd0hhWTJUdXpCa3JsQ1FNcjA1OUhHNHJaeU9JaEZNYXdyRDVnd0t3YkxuclZ1algxVHBsekp0MENDREcvK2d1UWlYR3F2NzlRTkJZN08vWnpvaUhmYmFCUDBFc3ZUNFkyTVJmSkQwbU4rZ2wzbllBQW5MVDlwSVQyWktuT3V5VTZCVFc2NGJLRWhHTkRtbUUycG8wQjhuNllRd0s3cGIrTllZMnlCQVAxVGg2UWoyUzIrSE9ZZDVqOUFFVkhQU1Q2N24yTmJua2RGOFJLYndnd3EzK1B2MHp0eWJ3MFRiOVdlb1pVZGg2dXMrV0MramRhOUZseTMvUktRc2dOT2JXSi9jelNyYW0xOVd3NXo0YW9NaVpvbFJkaVd5Q3ZvU0FMb214bW1CVmtOanhmczE0UnN4OURrTzg0TGloMG5PaVlsWXR4SHQ1YnBVZ1QwU2dKakgvcHFDb0Zrd25lYVlVaURoaVZuMzg2UVVkaU8zUGovdEtXTUlOWFFTN25RNytxNkVYS1YrckVSYjlwUy9RRjFLdjMzYzMwYVJJT1VlSGlDRElYKzJyQ3lJbTJIbzRRaG41ZUdXdzNMNVNQVEhhY1hRanVnSTlRQVh5TmNMTUc5SXpLanB5Mit1aFVaUDMralZiYzZmblBYWklmRkMydnl6UzVQTlZxclVRRzNUWTRQc1lSL202OFJLSi9Ia3FvQ1ZqRm8wVk9zODl4RnIyUDdtdlk3a1FkYStuak9Ub08xeHBGR0g4TWRlYmc0Uml0aFMrQU9qcC9wZDNnNlQ1TzNoK2FReXpXZ013anhZUGN4T0NxSDh1UG51RzlpUmY0ZGdOZ1ZDd1I5dm1OeElNNTdUQi9qT05iOWdqNmt0UGJaaFZ5bmxNVWhyRUdSVC9FRytsOVpiQzc0TlBFRE9aby9MYTAvY004MDVmaXZ3UVFCc1Q5ZjBMWWYrU1pSZGZPZTVnaU42S2JYUEJkalJSODNPRXpHbHhCaCtNbmRIQWNwdVRGZWxHTUR4QmNsa0VjWDdueVBUWUpkNlpOZUNvZEpDUHMzcWtsa1pUUkwrcHVxRVZaR1VVU1R4azU4OWhZRzNJTU8yWXFtMzYxcTYrNzRBNzNBR3I4RjBhZGJZODZCNTMwdmJaaGNFcUtLSUlDUDBuVDNhYy9iOUpWcHo0WFQ4NGxReSt3OEphaFJwcDZ2bEY5L0FLS0ZzYkpIZFpoMFFVR3B1Q2JlN284Y1J2c3c4c1pkMzdvNHh3STk5aHpiTDZ5bUc5TWE1RVVBRnRhM0tkUUszYmZNZnBQb0oyU255TEZXamFFRTVITFRuNmFScllyT25xWGloUTBBelNoUU1HL0M3N01TTHFsNU8rdEhUb09kZVlUMC9Id3NacTJWOTVacC9PZ0RJY0pwN0hGbE5jQ2hHd1ZJMXFIWlFmMFFjZnRjbnFWcVlsN3hyczI3eTB4K29WYitML0tEdlo0NGluUW16eHlxSUFSc2tIOGU3S0dMZXN2aXloYU9FaGxuam9ldUIxNTVtTGVRSmJuc3FHYytXMElIM081K0IvVDVKZ1VRdFN4eGVKUXptZS9nUWN0b2JkdkdnVmtsRkRrMW1qYTVpOHRwb1VFOGcyeWdVNEdra0huZUxEQUdqY2JYN1FZb0FtRDgraVBHNkovR0I0OS9vblFPajRPSy9HNlZZcnZuNWtHQjdxbCtxdE12cWJSdVk5ekZxUG5BYys2dDVyUTVHV2F6ZWI1YTgxREIyREc0NHdzNVJVcktYWWlHdlZneDNOTkFxRnpPNjBXUnlIM2dKK284MERsRFBNMU9wNHN5RUpPeDE5aGpKVHByb2E0aDFYemExOTQyUEFxVExDbjZLdC9RNk1EMERZRzV4dU5yaVUyd1pkeDRTYmZhYStxWGsxZFRYRUdTcVZEQ1pUbXdDRTh2a1dRMGI1ZTNhell0bEZFcHR2TTRXWmFJUVZxaXVqU05kbVVTU1ZLTE1yRFRIRUtJQ2daUE1PYTl5bUFEY3Q2by9VYURiTUpkNVpzZVI4NXpWUlpWKzdGd3pHVnZ4ZEE2cmYrclNvTHhwUFJkS0ZEeThZaWU3dHdLMk5GZGFCbkplQlFZWXYrWjZINGRyRFRaNWQ2dHRxcUlmUmVhcGNNOTYxaFRvcTFoemhGb1hOZlJxb3p1ZzRPSmlrcWxKVGVpMEc3cmpWclhQb3B2SDdkVTMwWXVYeGR0U0FkY2FoazlyVXV1MlMvWSsrWlpnYWJZMVpOYzlaTzFKeW55MzlDTGVEMEd4aVZPT24zWHlYcVl1bTRBbHBwRXEvdytYWHd6S1JvRXJ2NktPU1ptN0VsZHRQK0FtZmlTTUxNeVhPR1JEZGhLWVJ2WjlJUjhEUlJqTGdsUFplNEVoNHdSREVCTERMM0YrRVhVdEtzNFRlcGtHbENFRjZvSXpMc2FQQ3Jud29DdHJ2eTl6dGFzUzJ0UXBYSFNjcldWYjlZbTlDSFBQMGpNQlN4Z3g2MEFxSk5yeFRsV0pxR3JOWWVlYldRclJSQStTYmJwSWxVYkQ2V01NeldDdjNmVHRKcmlsSHhGT0FOaGFVVHl0QWhOM2lwZnB5NEIvNnhUM1VYVHRVQk04cjl0K2dNV3JRQ3E3b1o0Q3htOWhHdUV1TXlQUmVGTEZ2Tkh6d0ovdHlIK1VzVlYwRnI1SDZpWTlrSEhGek9NSGxTRDBLTy91d3FZL3RmM1kwRXN3TDBXUmtVcGg1UEdDelZZSDF1N05RR3JhOCtSMVlkMmxtMFgxQjdWb1RDREF3OXBoaTZtZ0IzbGpNRzFoSjJsWUlMMlBqTmIvNjVWL0lud1FHbDlRQ2J4SURqZ0tLVW03VEZvQjBYWVFCQ3ZNTk13Nm5BQnNiSkRhMkY0ekRiQ0E4a1VQZEtzWmZDM2xmb2RuaU1HeXBNRUthbXd0Q1pGODJEWS9NdHhYWEZaYnYrZUhKYWhjaG1WVFhPeERoUXU4K3pOWGRlc2tEZ0Q4ZjBZTWxzQ1lWMm84NDUrcGg0REsyQ25OM2ZFZ2RCdEZxdlRNTmxVWERWc0swUVVCdTkwcktXNVdMR3pGRnlpNXNaMWFBbUsvK3JhMjF2QXJVL09lVndNZng3a3NOc2JzalltVVJBMjFxN21iM0RkY2VzOUNKR3hxWEs4WS9rR2hIUUU5dnVDRzk4STR1a05qSURXclZVTmVDdTEvZlpQSmpOMmwzRG9WYVZjWmRuTDFTYlFncnFIM1dyVWs3SHhnVDhYSVllWVVFamJHcHRkaktlUTBOWEdwVU1LV0ZJdGRKci81aUo2aFQ1VjdOaTQ2aVF6RlFSdGFQKzdIaWpuSy9CUlJwbUhpRzRldTZDRHBoYVhGenpuVkdaY2FoU09qMFpuMndBQjQveVFKNjNCYzdETDF5OTYvR2poVUZ5bXRaak1ESDMrc085VW5CN045K1dGdlNBb2pxRFJaUjBBclN5M2Q1TWNTZFZrYnExTTlYNE5EQi9TNytManRLbjMrZ3hMeis3SXlZYWVGNEx0Z1dka1NRbUQzVVdYbmZxNXl6dDFEVTd5RXFicDBsbXpHamZJaGxMQ3hwMVFibHl5VEpmYS9DSS8ySnZzYllaSytLUzNYcGZ1WkUrQzRpR0x2aEhjdkVZeEY3OGFSNzgrSGFhbHo2UWphRk1xZ3pxMGZLSFF3Nm5wbTZQODVWSFpkQ0IxOFpQSDUybW13VWZQTktXanV6bkZGa3REQUcyeGRGRC9TZGVuU0h3OEdVSkNUT2FrenFxZ09LTmhHT0RqMitBR1RLMFd5Z2RmWndtWHR6RUFDdVlJMkV3ZmRKMk52b1E4aVY0TU1PcWQzbWVzUnBTWFNaRkhvbmpDWFp3TWFmNm14TnY0dz09MDN1RnZ5WS9zZzIrT2p1RCIsImV4cCI6MTY0NTkwODgxNCwic2hhcmRfaWQiOjgyMDc4NjA4NiwicGQiOjB9._GwCWq6aYQmMWAO70wwo_eGTPmJvW_BsARFGQjjUeOs",
    "fiche": "storycraft-meilleur-serveur-survie-1-18-1-nouvelles-grottes-6911",
    "referer": "https://storycraft.fr/"
} 

response = s.get("https://serveur-prive.net/minecraft/storycraft-meilleur-serveur-survie-1-18-1-nouvelles-grottes-6911/vote")

final = s.post("https://serveur-prive.net/template/ajax/vote.php", data=hd)
print(final.text)
#print(final.headers)
print(final.reason)