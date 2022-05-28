# data = [line.strip('\n') for line in open(r'C:\Users\red\Desktop\cow_frame.txt', 'r+', encoding='utf-8')]
# output = open(r'C:\Users\red\Desktop\new_countries_2.txt', 'a', encoding='utf-8')

print('''
1  Afghanistan
2  Åland Islands
3  Albania
4  Algeria
5  American Samoa
6  Andorra
7  Angola
8  Anguilla
9  Antigua and Barbuda
10  Argentina
11  Armenia
12  Aruba
13  Australia
14  Austria
15  Azerbaijan
16  Bahamas
17  Bahrain
18  Bangladesh
19  Barbados
20  Belarus
21  Belgium
22  Belize
23  Benin
24  Bermuda
25  Bhutan
26  Bolivia, Plurinational State of
27  Bosnia and Herzegovina
28  Botswana
29  Bouvet Island
30  Brazil
31  Brunei Darussalam
32  Bulgaria
33  Burkina Faso
34  Burundi
35  Cambodia
36  Cameroon
37  Canada
38  Cape Verde
39  Cayman Islands
40  Central African Republic
41  Chad
42  Chile
43  China
44  Christmas Island
45  Colombia
46  Comoros
47  Congo
48  Congo, The Democratic Republic of the
49  Cook Islands
50  Costa Rica
51  Côte d'Ivoire
52  Croatia
53  Cuba
54  Curaçao
55  Cyprus
56  Czech Republic
57  Denmark
58  Djibouti
59  Dominica
60  Dominican Republic
61  Ecuador
62  Egypt
63  El Salvador
64  Equatorial Guinea
65  Eritrea
66  Estonia
67  Ethiopia
68  Falkland Islands (Malvinas)
69  Faroe Islands
70  Fiji
71  Finland
72  France
73  French Guiana
74  Gabon
75  Gambia
76  Georgia
77  Germany
78  Ghana
79  Gibraltar
80  Greece
81  Greenland
82  Grenada
83  Guadeloupe
84  Guam
85  Guatemala
86  Guernsey
87  Guinea
88  Guinea-Bissau
89  Guyana
90  Haiti
91  Heard Island and McDonald Islands
92  Holy See (Vatican City State)
93  Honduras
94  Hong Kong
95  Hungary
96  Iceland
97  India
98  Indonesia
99  Iran, Islamic Republic of
100  Iraq
101  Ireland
102  Isle of Man
103  Israel
104  Italy
105  Jamaica
106  Japan
107  Jersey
108  Jordan
109  Kazakhstan
110  Kenya
111  Kiribati
112  Korea, Democratic People's Republic of
113  Korea, Republic of
114  Kuwait
115  Kyrgyzstan
116  Lao People's Democratic Republic
117  Latvia
118  Lebanon
119  Lesotho
120  Liberia
121  Libyan Arab Jamahiriya
122  Liechtenstein
123  Lithuania
124  Luxembourg
125  Macao
126  Macedonia, The Former Yugoslav Republic of
127  Madagascar
128  Malawi
129  Malaysia
130  Maldives
131  Mali
132  Malta
133  Marshall Islands
134  Martinique
135  Mauritania
136  Mauritius
137  Mayotte
138  Mexico
139  Micronesia, Federated States of
140  Moldova, Republic of
141  Monaco
142  Mongolia
143  Montenegro
144  Montserrat
145  Morocco
146  Mozambique
147  Myanmar
148  Namibia
149  Nauru
150  Nepal
151  Netherlands
152  New Caledonia
153  New Zealand
154  Nicaragua
155  Niger
156  Nigeria
157  Niue
158  Norfolk Island
159  Northern Mariana Islands
160  Norway
161  Oman
162  Pakistan
163  Palau
164  Panama
165  Papua New Guinea
166  Paraguay
167  Peru
168  Philippines
169  Pitcairn
170  Poland
171  Portugal
172  Puerto Rico
173  Qatar
174  Réunion
175  Romania
176  Russian Federation
177  Rwanda
178  Saint Barthélemy
179  Saint Kitts and Nevis
180  Saint Lucia
181  Saint Martin (French part)
182  Saint Pierre and Miquelon
183  Saint Vincent and The Grenadines
184  Samoa
185  San Marino
186  Sao Tome and Principe
187  Saudi Arabia
188  Senegal
189  Serbia
190  Seychelles
191  Sierra Leone
192  Singapore
193  Sint Maarten (Dutch part)
194  Slovakia
195  Slovenia
196  Solomon Islands
197  Somalia
198  South Africa
199  South Georgia and the South Sandwich Islands
200  South Sudan
201  Spain
202  Sri Lanka
203  Sudan
204  Suriname
205  Svalbard and Jan Mayen
206  Swaziland
207  Sweden
208  Switzerland
209  Syrian Arab Republic
210  Taiwan, Province of China
211  Tajikistan
212  Tanzania, United Republic of
213  Thailand
214  Timor-Leste
215  Togo
216  Tokelau
217  Tonga
218  Trinidad and Tobago
219  Tunisia
220  Turkey
221  Turkmenistan
222  Turks and Caicos Islands
223  Tuvalu
224  Uganda
225  Ukraine
226  United Arab Emirates
227  United Kingdom
228  United States
229  Uruguay
230  Uzbekistan
231  Vanuatu
232  Venezuela, Bolivarian Republic of
233  Viet Nam
234  Virgin Islands, British
235  Virgin Islands, U.S.
236  Wallis and Futuna
237  Western Sahara
238  Yemen
239  Zambia
240  Zimbabwe

''')
country_code = int(input('please select number of country: '))
print(country_code)










# def clear_data():
#     new_data = []
#     for countries in data:
#         new_data.append(countries.split(';'))
#     for i in new_data:
#         x = 1
#         print(i[6], i[66], i[64], i[65], i[63], file=output)
#     output.close()
#
#
# clear_data()
# last_shit = open(r'C:\Users\red\Desktop\new_countries_last.txt', 'a')
# with open(r'C:\Users\red\Desktop\new_countries_2.txt', 'r') as hello:
#     for i, v in enumerate(hello.readlines(), 1):
#         print(i, v, end="", file=last_shit)
