import requests, json, csv

indicators = ["covid","mask","contact","finance","covid_vaccine","trust_who","trust_govt", "concerned_sideeffects", \
    "hesitant_sideeffects", "modified_acceptance", "access_wash","wash_hands_24h_3to6","wash_hands_24h_7orMore","cmty_covid"]

countries = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', \
    'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Burkina Faso', \
    'Cambodia', 'Cameroon', 'Canada', 'Chile', 'Colombia', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Czech Republic', \
    'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Finland', 'France', 'Germany', \
    'Ghana', 'Greece', 'Guatemala', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'India', 'Indonesia', 'Iraq', \
    'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Lebanon', \
    'Libya', 'Malaysia', 'Mali', 'Mexico', 'Moldova', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Netherlands',\
    'New Zealand', 'Nicaragua', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Paraguay', \
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico, U.S.', 'Qatar', 'Romania', 'Russia', 'Saudi Arabia',\
    'Senegal', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka',\
    'Sudan', 'Sweden', 'Switzerland', 'Taiwan', 'Tanzania', 'Thailand', 'Tunisia', 'Turkey', 'Ukraine', \
    'United Arab Emirates','United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen']

sorted_column_names = [['smoothed_cli', 'smoothed_cli_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_mc', 'smoothed_mc_se', 'sample_size_mc', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_dc', 'smoothed_dc_se', 'sample_size_dc', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_hf', 'smoothed_hf_se', 'sample_size_hf', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_covid_vaccine', 'smoothed_covid_vaccine_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_sideeffects', 'smoothed_sideeffects_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_hesitant_sideeffects', 'smoothed_hesitant_sideeffects_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_modified_acceptance', 'smoothed_modified_acceptance_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_trust_who', 'smoothed_trust_who_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_trust_govt', 'smoothed_trust_govt_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_access_wash', 'smoothed_access_wash_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_wash_hands_24h_3to6', 'smoothed_wash_hands_24h_3to6_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_wash_hands_24h_7ormore', 'smoothed_wash_hands_24h_7ormore_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date'],
    ['smoothed_community_cli', 'smoothed_community_cli_se', 'sample_size', 'country', 'iso_code', 'gid_0', 'survey_date']]

with open('testing.csv', mode='w',newline='') as csv_file:
    
    writer = csv.DictWriter(csv_file, fieldnames=sorted_column_names)
    writer.writeheader()
    for indicator in indicators:
        column_names = sorted_column_names[indicators.index(indicator)]
        for country in countries:
            response = requests.get("https://covidmap.umd.edu/api/resources?indicator=" + indicators \
                + "&type=smoothed&country=" + country + "&daterange=20200423-20210223")
            res = response.text
            jsonData = json.loads(res)

            if "data" in jsonData:
                jsonData = jsonData["data"]
                for dicts in jsonData:
                    writer.writerow(dicts)
            response.close()
