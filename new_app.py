import streamlit as st
import streamlit.components.v1 as components


import pandas as pd
import numpy as np
import pickle
import requests, os
import base64

apptitle = 'Gov Contracts'
st.set_page_config(page_title=apptitle, page_icon=":book:")


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.75)), url("data:image/png;base64,%s");
    background-size:cover;
    background-repeat:no-repeat;
    position: absolute;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background("Images/GovernmentContract_4.png")

#with open("Images/uicbusiness.png", "rb") as f:
 #   data = base64.b64encode(f.read()).decode("utf-8")
  #  st.markdown(
   # f"""
    #<div style="margin-top:-.5%;margin-left:-5%;">
    #<img src="data:image/png;base64,{data}" width="200" height="100">
    #</div>
    #""",
    #unsafe_allow_html=True,
#)

def intro():
    import streamlit as st
    import streamlit.components.v1 as components

    import pandas as pd
    import numpy as np
    import pickle
    import requests, os
    import base64

    st.write("# Government Contracts in the Pandemic Era: A Comprehensive Analysis")
    st.sidebar.success("Select an option above.")

    st.markdown(
        """
        WELCOME!

        Government Contracts are contracts that are given to various 
        vendors to complete the task at hand. There are some contracts 
        that are released everyday depending on the need of the related 
        government agency.
        
        One of the websites to get updated government contracts related 
        information is [sam.gov](https://sam.gov/content/home)
       
        If you are a vendor for government contracts and want to see 
        details about the contract assignments, then you are at the 
        right place!
        
        👈 Select an option from the dropdown on the left to see the predictions for Business Type, Contract Value and Contract duration
    """
    )

    
    st.write("# ------------------------------------------------")
    st.write("Project Collaborators")

    linkedin_imgs = [
        "Images/l4-modified.png",
        "Images/l2-modified.png",
        "Images/l5-modified.png",
        "Images/l1-modified.png",
        "Images/l3-modified.png",
    ]


    idx=0
    for idx, img in enumerate(linkedin_imgs): 
        cols = st.columns(5) 
        cols[0].image(linkedin_imgs[idx], use_column_width=True)
        cols[0].markdown('<a href="https://www.linkedin.com/in/nabila-rg/">Nabila Fakhruddin</a>', unsafe_allow_html=True)
        idx+=1
        cols[1].image(linkedin_imgs[idx], use_column_width=True)
        cols[1].markdown('<a href="https://www.linkedin.com/in/sunaina-tarimela-b45139113">Sunaina Tarimela</a>', unsafe_allow_html=True)
        idx+=1
        cols[2].image(linkedin_imgs[idx], use_column_width=True)
        cols[2].markdown('<a href="https://www.linkedin.com/in/vojtech-mensik-42a4391a1/">Vojtech Mensik</a>', unsafe_allow_html=True)
        idx+=1
        cols[3].image(linkedin_imgs[idx], use_column_width=True)
        cols[3].markdown('<a href="https://www.linkedin.com/in/aarshvyas/">Aarsh Vyas</a>', unsafe_allow_html=True)
        idx+=1
        cols[4].image(linkedin_imgs[idx], use_column_width=True)
        cols[4].markdown('<a href="https://www.linkedin.com/in/janhavigulabani/">Janhavi Gulabani</a>', unsafe_allow_html=True)
        break

    st.markdown("""
        This project has been completed under the guidance of our professor, [Dr.Fatemeh Sarayloo](https://business.uic.edu/profiles/sarayloo-fatemeh/)
        """
        )


def business_type_predict():
    import pandas as pd
    import numpy as np
    import pickle
    import requests, os
    import base64
    import streamlit as st
    import streamlit.components.v1 as components
    from streamlit.components.v1 import html


    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.75)), url("data:image/png;base64,%s");
        background-size:cover;
        background-repeat:no-repeat;
        position: absolute;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
    set_background("Images/GovernmentContract_BT.png")

    def construct_sample(input):

        # Load the serialized object from the pickle file
        with open('Pickle/label_encoder.pkl', 'rb') as file:
          label_encoders = pickle.load(file)

        X_test = np.zeros(20)
        X_test[0] = label_encoders['Contracting Agency ID'].transform([input[0]])
        X_test[1] = label_encoders['Domestic or Foreign Entity'].transform([input[5]])
        X_test[2] = label_encoders['Is Performance Based Service Acquisition'].transform([input[6]])
        X_test[3] = label_encoders['Type of Contract'].transform([input[1]])
        X_test[4] = label_encoders['NAICS Code'].transform([input[2][:2]])
        X_test[5] = label_encoders['Principal Place of Performance State Code'].transform([input[3]])
        X_test[6] = label_encoders['Principal Place of Performance Country Name'].transform([input[4]])
        X_test[7] = label_encoders['Country of Product or Service Origin'].transform([input[19]])
        X_test[8] = label_encoders['Extent Competed'].transform([input[7]])
        X_test[9] = label_encoders['Solicitation Procedures'].transform([input[8]])
        X_test[10] = label_encoders['Local Area Set Aside'].transform([input[9]])
        X_test[11] = label_encoders['Vendor Address State Name'].transform([input[10]])
        X_test[12] = label_encoders['Vendor Address Country Name'].transform([input[11]])
        X_test[13] = label_encoders['Labor Standards'].transform([input[12]])
        X_test[14] = label_encoders['Is Vendor Business Type - For Profit Organization'].transform([input[13]])
        X_test[15] = label_encoders['Is Vendor Business Type - All Awards'].transform([input[14]])
        X_test[16] = label_encoders['Is Vendor Business Type - Corporate Entity, Not Tax Exempt'].transform([input[15]])
        X_test[17] = label_encoders['Is Vendor Business Type - Manufacturer Of Goods'].transform([input[16]])
        X_test[18] = label_encoders['Base and All Options Value (Total Contract Value)'].transform(np.array([input[17]]).reshape(-1, 1))
        X_test[19] = label_encoders['Duration of Contract'].transform(np.array([input[18]]).reshape(-1, 1))

        return X_test

    def run_pred_model_business_type (select_agencyid : str,select_contracttype : str,select_naicscode : str,select_pricipalplaceofperformancestate : str,select_pricipalplaceofperformancecountry: str,select_entity: str,select_performancebasedservice: str,select_extentcompeted: str,select_solicitationprocedures: str,select_localareasetaside: str,select_vendoraddresstatename: str,select_vendoraddresscountryname: str,select_laborstandards: str,select_vendorbusinesstypeforProfit: str,select_vendorbusinesstypeallawards: str,select_vendorbusinesstypecorprateentity: str,select_vendorbusinesstypeManufactofgoods: str,select_contractvalue: str,select_contractduration: str,select_countryofprodservorigin: str):


        #Generate prediction
        input = [select_agencyid,select_contracttype,select_naicscode,select_pricipalplaceofperformancestate,select_pricipalplaceofperformancecountry,
                        select_entity,select_performancebasedservice,select_extentcompeted,select_solicitationprocedures,select_localareasetaside,
                        select_vendoraddresstatename,select_vendoraddresscountryname,select_laborstandards,select_vendorbusinesstypeforProfit,
                        select_vendorbusinesstypeallawards,select_vendorbusinesstypecorprateentity,select_vendorbusinesstypeManufactofgoods,
                        select_contractvalue,select_contractduration, select_countryofprodservorigin]

        X_test = construct_sample(input)

        # Load the serialized object from the pickle file
        with open('Pickle/clf.pkl', 'rb') as file:
          loaded_model = pickle.load(file)

        prediction = loaded_model.predict(X_test.reshape(1, -1) )
       
        # Load the serialized object from the pickle file
        with open('Pickle/label_encoder.pkl', 'rb') as file:
          label_encoders = pickle.load(file)
       
        #Predicted Business Type
        BusinessType = label_encoders['Business Type'].inverse_transform([prediction])
        # return BusinessType
        list_result = []
        list_result.append(BusinessType)

        #Predict Probabilities
        pred_probabilities = loaded_model.predict_proba(X_test.reshape(1, -1))

        # Load the serialized object from the pickle file
        with open('Pickle/label_encoder.pkl', 'rb') as file:
          label_encoders = pickle.load(file)

        prob_df=pd.DataFrame(pred_probabilities, columns=label_encoders['Business Type'].classes_)
        # return prob_df
        list_result.append(prob_df)

        return list_result

        # #Predicted Business Type
        # #BusinessType = label_encoders['Business Type'].inverse_transform([prediction])
        # #return BusinessType

        # #Predict Probabilities
        # pred_probabilities = loaded_model.predict_proba(X_test.reshape(1, -1))


        # # Load the serialized object from the pickle file
        # with open('Pickle/label_encoder.pkl', 'rb') as file:
        #   label_encoders = pickle.load(file)

        # prob_df=pd.DataFrame(pred_probabilities, columns=label_encoders['Business Type'].classes_)
        # return prob_df


    #tableau_dashboard_url = "https://public.tableau.com/views/IDS_560_dashboard/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link"

    # Create a clickable link that opens in a new tab
    #st.markdown(f'[Open Tableau Dashboard]({tableau_dashboard_url}){:target="_blank"}', unsafe_allow_html=True)

    st.write("# Predicting the Business Type that will win the contract")
    st.markdown(
        """
        Before predicting the Business Type to win the contract, you can see the latest trands and visualizations by clicking on the link provided.
        """
        )
    def open_page(url):
        open_script= """
        <script type="text/javascript">
             window.open('%s', '_blank').focus();
        </script>
        """ % (url)
        html(open_script)

    st.button('Click to view tableau dashboard', on_click=open_page, args=('https://public.tableau.com/views/IDS560_dashboard_N/Story1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link',))

    
    st.markdown(
        """
            Let's now predict which Business Type will win the contract.
            Please fill out the fields on the left and click on the button below to see the output.
            You will also see the probability of other Business Types winning a contract with the inputs provided.

        """
        )
    
    #-- Set business type

    select_agencyid = st.sidebar.text_input(label="Contracting Agency ID", placeholder="1406")

    select_contracttype = st.sidebar.selectbox('Contract Type',
                                        ['FIRM FIXED PRICE','TIME AND MATERIALS','LABOR HOURS','FIXED PRICE AWARD FEE','FIXED PRICE WITH ECONOMIC PRICE ADJUSTMENT','COST NO FEE','COST PLUS FIXED FEE','COST PLUS AWARD FEE','COST PLUS INCENTIVE FEE','FIXED PRICE INCENTIVE','FIXED PRICE LEVEL OF EFFORT','COST SHARING','FIXED PRICE REDETERMINATION'])

    select_naicscode = st.sidebar.text_input(label="NAICS Code", placeholder="622109")

    #select_pricipalplaceofperformancestate = st.sidebar.selectbox('Principal place of performance state code', ['VA','DC','CA','MD','IN','FL','NY','MO','CO','AK','LA','ID','WY','SD','MT','OR','WA','VT','PA','NM','NJ','IL','MN','TX','WV','AL','PR','KY','SC','NC','OK','GA','AR','MS','NE','MI','OH','IA','DE','NH','KS','WI','AZ','TN','CT','MA','HI','UT','RI','ME','ND','NV','AS','UGANDA','GU','FRANCE','VI','VIETNAM','CANADA','JAPAN','INDIA','CANADA','MEXICO'])
    select_pricipalplaceofperformancestate = st.sidebar.selectbox('Principal place of performance state code', ['VA',	'DC',	'CA',	'MD',	'IN',	'FL',	'NY',	'MO',	'CO',	'AK',	'LA',	'ID',	'WY',	'SD',	'MT',	'OR',	'WA',	'VT',	'PA',	'NM',	'NJ',	'IL',	'MN',	'TX',	'WV',	'AL',	'PR',	'KY',	'SC',	'NC',	'OK',	'GA',	'AR',	'MS',	'NE',	'MI',	'OH',	'IA',	'DE',	'NH',	'KS',	'WI',	'AZ',	'TN',	'CT',	'MA',	'HI',	'UT',	'RI',	'ME',	'ND',	'NV',	'AS',	'UGANDA',	'GU',	'FRANCE',	'VI',	'VIETNAM',	'CANADA',	'JAPAN',	'UNITED KINGDOM',	'BAHRAIN',	'DJIBOUTI',	'SPAIN',	'ITALY',	'GREECE',	'SINGAPORE',	'SRI LANKA',	'BANGLADESH',	'SAMOA',	'PHILIPPINES',	'CAMBODIA',	'MICRONESIA, FEDERATED STATES OF',	'MONGOLIA',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'LAOS',	'MP',	'AUSTRALIA',	'CROATIA',	'ROMANIA',	'CUBA',	'INDIA',	'IRAQ',	'ANGOLA',	'AFGHANISTAN',	'ALGERIA',	'AZERBAIJAN',	'ALBANIA',	'CENTRAL AFRICAN REPUBLIC',	'HONDURAS',	'ISRAEL',	'THAILAND',	'KOREA, SOUTH',	'PERU',	'URUGUAY',	'JAMAICA',	'SOUTH SUDAN',	'BAHAMAS, THE',	'ERITREA',	'NAMIBIA',	'MOROCCO',	'GERMANY',	'SOMALIA',	'JORDAN',	'CAMEROON',	'POLAND',	'MOZAMBIQUE',	'SAUDI ARABIA',	'DOMINICAN REPUBLIC',	'LEBANON',	'CONGO (KINSHASA)',	'TURKEY',	'NEW ZEALAND',	'CONGO (BRAZZAVILLE)',	'TURKMENISTAN',	'GUYANA',	'PARAGUAY',	'CYPRUS',	'SUDAN',	'GUATEMALA',	'KENYA',	'ARGENTINA',	'SOUTH AFRICA',	'BOTSWANA',	'BELGIUM',	'BURMA',	'BRAZIL',	'BURUNDI',	'COLOMBIA',	'CHILE',	'CHINA',	'COSTA RICA',	'IRELAND',	'ECUADOR',	'EL SALVADOR',	'ETHIOPIA',	'CZECHIA',	'FIJI',	'AUSTRIA',	'SLOVENIA',	'UZBEKISTAN',	'SLOVAKIA',	'NORTH MACEDONIA',	'BULGARIA',	'KOSOVO',	'RWANDA',	'GEORGIA',	'KAZAKHSTAN',	'UKRAINE',	'SENEGAL',	'ARMENIA',	'NIGERIA',	'BELARUS',	'ESWATINI',	'MOLDOVA',	'LATVIA',	'NIGER',	'MONTENEGRO',	'BURKINA FASO',	'LESOTHO',	'LITHUANIA',	'EGYPT',	'GABON',	'CHAD',	'PANAMA',	'UNITED ARAB EMIRATES',	'LIBERIA',	'MALAWI',	'MAURITIUS',	'MAURITANIA',	'OMAN',	'CURACAO',	'PAKISTAN',	'PAPUA NEW GUINEA',	'SERBIA',	'TUNISIA',	'TIMOR-LESTE',	'SWITZERLAND',	'ICELAND',	'BOSNIA AND HERZEGOVINA',	'KUWAIT',	'UNITED STATES MINOR OUTLYING ISLANDS',	'GUANTANAMO BAY NAVAL BASE',	'MEXICO',	'GREENLAND',	'PORTUGAL',	'QATAR',	'SYRIA',	'ZIMBABWE',	'TANZANIA',	'GHANA',	'GUINEA',	'MALI',	'DENMARK',	'SWEDEN',	'NETHERLANDS',	'BENIN',	'CABO VERDE',	'SOLOMON ISLANDS'])
   
    #select_pricipalplaceofperformancecountry = st.sidebar.selectbox('Principal place of performance country name',
                                        #['UNITED STATES','UGANDA','FRANCE','VIETNAM','CANADA','JAPAN','UNITED KINGDOM','BAHRAIN','INDIA','CANADA','MEXICO'])
    select_pricipalplaceofperformancecountry = st.sidebar.selectbox('Principal place of performance country name',
                                        ['UNITED STATES',	'UGANDA',	'FRANCE',	'VIETNAM',	'CANADA',	'JAPAN',	'UNITED KINGDOM',	'BAHRAIN',	'DJIBOUTI',	'SPAIN',	'ITALY',	'GREECE',	'SINGAPORE',	'SRI LANKA',	'BANGLADESH',	'SAMOA',	'PHILIPPINES',	'CAMBODIA',	'MICRONESIA, FEDERATED STATES OF',	'MONGOLIA',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'LAOS',	'AUSTRALIA',	'CROATIA',	'ROMANIA',	'CUBA',	'INDIA',	'IRAQ',	'ANGOLA',	'AFGHANISTAN',	'ALGERIA',	'AZERBAIJAN',	'ALBANIA',	'CENTRAL AFRICAN REPUBLIC',	'HONDURAS',	'ISRAEL',	'THAILAND',	'KOREA, SOUTH',	'PERU',	'URUGUAY',	'JAMAICA',	'SOUTH SUDAN',	'BAHAMAS, THE',	'ERITREA',	'NAMIBIA',	'MOROCCO',	'GERMANY',	'SOMALIA',	'JORDAN',	'CAMEROON',	'POLAND',	'MOZAMBIQUE',	'SAUDI ARABIA',	'DOMINICAN REPUBLIC',	'LEBANON',	'CONGO (KINSHASA)',	'TURKEY',	'NEW ZEALAND',	'CONGO (BRAZZAVILLE)',	'TURKMENISTAN',	'GUYANA',	'PARAGUAY',	'CYPRUS',	'SUDAN',	'GUATEMALA',	'KENYA',	'ARGENTINA',	'SOUTH AFRICA',	'BOTSWANA',	'BELGIUM',	'BURMA',	'BRAZIL',	'BURUNDI',	'COLOMBIA',	'CHILE',	'CHINA',	'COSTA RICA',	'IRELAND',	'ECUADOR',	'EL SALVADOR',	'ETHIOPIA',	'CZECHIA',	'FIJI',	'AUSTRIA',	'SLOVENIA',	'UZBEKISTAN',	'SLOVAKIA',	'NORTH MACEDONIA',	'BULGARIA',	'KOSOVO',	'RWANDA',	'GEORGIA',	'KAZAKHSTAN',	'UKRAINE',	'SENEGAL',	'ARMENIA',	'NIGERIA',	'BELARUS',	'ESWATINI',	'MOLDOVA',	'LATVIA',	'NIGER',	'MONTENEGRO',	'BURKINA FASO',	'LESOTHO',	'LITHUANIA',	'EGYPT',	'GABON',	'CHAD',	'PANAMA',	'UNITED ARAB EMIRATES',	'LIBERIA',	'MALAWI',	'MAURITIUS',	'MAURITANIA',	'OMAN',	'CURACAO',	'PAKISTAN',	'PAPUA NEW GUINEA',	'SERBIA',	'TUNISIA',	'TIMOR-LESTE',	'SWITZERLAND',	'ICELAND',	'BOSNIA AND HERZEGOVINA',	'KUWAIT',	'UNITED STATES MINOR OUTLYING ISLANDS',	'GUANTANAMO BAY NAVAL BASE',	'MEXICO',	'GREENLAND',	'PORTUGAL',	'QATAR',	'SYRIA',	'ZIMBABWE',	'TANZANIA',	'GHANA',	'GUINEA',	'MALI',	'DENMARK',	'SWEDEN',	'NETHERLANDS',	'BENIN',	'CABO VERDE',	'SOLOMON ISLANDS'])

    select_entity = st.sidebar.selectbox("Domestic or Foreign Entity",['U.S. OWNED BUSINESS','OTHER U.S. ENTITY (E.G. GOVERNMENT)','FOREIGN-OWNED BUSINESS INCORPORATED IN THE U.S.','FOREIGN-OWNED BUSINESS NOT INCORPORATED IN THE U.S.','OTHER FOREIGN ENTITY (E.G. FOREIGN GOVERNMENT)'])

    select_performancebasedservice = st.sidebar.radio("Performance Based Service Acquisition",('NO - SERVICE WHERE PBA IS NOT USED.','YES - SERVICE WHERE PBA IS USED.','NOT APPLICABLE'))

    select_extentcompeted = st.sidebar.selectbox('Extent Competed',
                                        ['FULL AND OPEN COMPETITION','NOT COMPETED UNDER SAP','FULL AND OPEN COMPETITION AFTER EXCLUSION OF SOURCES','NOT COMPETED','COMPETED UNDER SAP','NOT AVAILABLE FOR COMPETITION'])

    select_solicitationprocedures = st.sidebar.selectbox('Solicitation Procedures',
                                        ['SUBJECT TO MULTIPLE AWARD FAIR OPPORTUNITY','SIMPLIFIED ACQUISITION','NEGOTIATED PROPOSAL/QUOTE','ONLY ONE SOURCE','ALTERNATIVE SOURCES','SEALED BID','ARCHITECT-ENGINEER FAR 6.102','BASIC RESEARCH','TWO STEP'])

    select_localareasetaside = st.sidebar.radio("Local Area Set Aside",('YES','NO'))

    select_vendoraddresstatename = st.sidebar.selectbox('Vendor Address State',
                                        ['VIRGINIA',	'MARYLAND',	'FLORIDA',	'RHODE ISLAND',	'CALIFORNIA',	'INDIANA',	'NEW YORK',	'NORTH CAROLINA',	'MINNESOTA',	'MISSOURI',	'ALASKA',	'TEXAS',	'PENNSYLVANIA',	'MISSISSIPPI',	'IDAHO',	'WYOMING',	'OREGON',	'DISTRICT OF COLUMBIA',	'MONTANA',	'WASHINGTON',	'MASSACHUSETTS',	'NEW JERSEY',	'ILLINOIS',	'WEST VIRGINIA',	'COLORADO',	'OHIO',	'ALABAMA',	'KENTUCKY',	'GEORGIA',	'OKLAHOMA',	'LOUISIANA',	'KANSAS',	'NEBRASKA',	'SOUTH CAROLINA',	'NEVADA',	'NEW MEXICO',	'WISCONSIN',	'SOUTH DAKOTA',	'ARKANSAS',	'ARIZONA',	'MICHIGAN',	'PUERTO RICO',	'CONNECTICUT',	'HAWAII',	'TENNESSEE',	'UTAH',	'VERMONT',	'IOWA',	'NEW HAMPSHIRE',	'MAINE',	'DELAWARE',	'NORTH DAKOTA',	'VIRGIN ISLANDS OF THE U.S.',	'GUAM',	'AMERICAN SAMOA',	'NORTHERN MARIANA ISLANDS',	'CANADA',	'FRANCE',	'UNITED KINGDOM',	'JAPAN',	'ROMANIA',	'SPAIN',	'ITALY',	'SINGAPORE',	'SRI LANKA',	'NEW ZEALAND',	'IRAQ',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'PHILIPPINES',	'VIETNAM',	'CROATIA',	'GREECE',	'UNITED ARAB EMIRATES',	'INDIA',	'BAHRAIN',	'BELGIUM',	'COLOMBIA',	'CAMBODIA',	'CONGO (KINSHASA)',	'COSTA RICA',	'FIJI',	'SLOVENIA',	'KENYA',	'UZBEKISTAN',	'MOROCCO',	'SLOVAKIA',	'BULGARIA',	'ALBANIA',	'KAZAKHSTAN',	'AZERBAIJAN',	'UKRAINE',	'SENEGAL',	'SOUTH AFRICA',	'THAILAND',	'NIGERIA',	'ARMENIA',	'LITHUANIA',	'BURUNDI',	'UGANDA',	'MOLDOVA',	'ALGERIA',	'ESTONIA',	'LATVIA',	'MOZAMBIQUE',	'RWANDA',	'CYPRUS',	'GABON',	'MONTENEGRO',	'NETHERLANDS',	'KOREA, SOUTH',	'NIGER',	'PANAMA',	'SERBIA',	'SOUTH SUDAN',	'SWITZERLAND',	'GERMANY',	'BOTSWANA',	'ICELAND',	'SAUDI ARABIA',	'POLAND',	'NORTH MACEDONIA',	'KOSOVO',	'BOSNIA AND HERZEGOVINA',	'PERU',	'KUWAIT',	'PORTUGAL',	'DENMARK',	'QATAR',	'GHANA',	'ISRAEL',	'MALI',	'SWEDEN',	'AUSTRALIA',	'AUSTRIA',	'JORDAN'])

    select_vendoraddresscountryname = st.sidebar.selectbox('Vendor address country name',
                                        ['UNITED STATES',	'CANADA',	'FRANCE',	'UNITED KINGDOM',	'JAPAN',	'ROMANIA',	'GUAM',	'SPAIN',	'ITALY',	'SINGAPORE',	'SRI LANKA',	'NEW ZEALAND',	'IRAQ',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'PHILIPPINES',	'VIETNAM',	'CROATIA',	'GREECE',	'UNITED ARAB EMIRATES',	'INDIA',	'BAHRAIN',	'BELGIUM',	'COLOMBIA',	'CAMBODIA',	'CONGO (KINSHASA)',	'COSTA RICA',	'FIJI',	'SLOVENIA',	'KENYA',	'UZBEKISTAN',	'MOROCCO',	'SLOVAKIA',	'BULGARIA',	'ALBANIA',	'GEORGIA',	'KAZAKHSTAN',	'AZERBAIJAN',	'UKRAINE',	'SENEGAL',	'SOUTH AFRICA',	'THAILAND',	'NIGERIA',	'ARMENIA',	'LITHUANIA',	'BURUNDI',	'UGANDA',	'MOLDOVA',	'ALGERIA',	'ESTONIA',	'LATVIA',	'MOZAMBIQUE',	'RWANDA',	'CYPRUS',	'GABON',	'MONTENEGRO',	'NETHERLANDS',	'KOREA, SOUTH',	'NIGER',	'PANAMA',	'SERBIA',	'SOUTH SUDAN',	'SWITZERLAND',	'GERMANY',	'BOTSWANA',	'ICELAND',	'SAUDI ARABIA',	'POLAND',	'NORTH MACEDONIA',	'KOSOVO',	'BOSNIA AND HERZEGOVINA',	'PERU',	'KUWAIT',	'PORTUGAL',	'DENMARK',	'QATAR',	'GHANA',	'ISRAEL',	'MALI',	'SWEDEN',	'AUSTRALIA',	'AUSTRIA',	'JORDAN'])

    select_laborstandards = st.sidebar.radio("Labor Standards",('YES','NO','NOT APPLICABLE'))

    select_vendorbusinesstypeforProfit = st.sidebar.radio("Is Vendor Business type - For Profit Organisation",('YES','NO'))

    select_vendorbusinesstypeallawards = st.sidebar.radio("Is Vendor Business type - All Awards ",('YES','NO'))

    select_vendorbusinesstypecorprateentity = st.sidebar.radio("Is Vendor Business type - Corporate Entity, Not tax Exempt",('YES','NO'))

    select_vendorbusinesstypeManufactofgoods = st.sidebar.radio("Is Vendor Business type - Manufacturer of Goods",('YES','NO'))

    select_contractvalue = st.sidebar.text_input(label="Total Contract Value", placeholder="$25,000,000")

    select_contractduration = st.sidebar.text_input(label="Contract Duration(in days)", placeholder="365")

    select_countryofprodservorigin = st.sidebar.selectbox('Country of Product or Service Origin',
                                        ['UNITED STATES','INDIA','CANADA','MEXICO'])


    #html_temp = "<div class='tableauPlaceholder' id='viz1711381846728' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ID&#47;IDS_560_dashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IDS_560_dashboard&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ID&#47;IDS_560_dashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1711381846728');                    var vizElement = divElement.getElementsByTagName('object')[0];                 if ( divElement.offsetWidth > 800 ) { vizElement.style.width='2850px';vizElement.style.height='1727px';}else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='2850px';vizElement.style.height='1727px';} else { vizElement.style.width='100%';vizElement.style.height='2077px';}               var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    #components.html(html_temp)

    def main():
      import pickle
      # Load the serialized object from the pickle file
      with open('Pickle/clf.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

      # # Load the serialized object from the pickle file
      with open('Pickle/label_encoder.pkl', 'rb') as file:
        label_encoders = pickle.load(file)



    #html_temp = "<div class='tableauPlaceholder' id='viz1710733360364' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ID&#47;IDS_560_dashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IDS_560_dashboard&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ID&#47;IDS_560_dashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1710733360364');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1620px';vizElement.style.maxWidth='1720px';vizElement.style.width='100%';vizElement.style.minHeight='818px';vizElement.style.maxHeight='910px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1620px';vizElement.style.maxWidth='1720px';vizElement.style.width='100%';vizElement.style.minHeight='818px';vizElement.style.maxHeight='910px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1250px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    #components.html(html_temp)

    if st.button ("Predict the business type to win the contract"):
        list_name = run_pred_model_business_type(select_agencyid,select_contracttype,select_naicscode,select_pricipalplaceofperformancestate,
                    select_pricipalplaceofperformancecountry,select_entity,select_performancebasedservice,select_extentcompeted,select_solicitationprocedures,
                    select_localareasetaside,select_vendoraddresstatename,select_vendoraddresscountryname,select_laborstandards,
                    select_vendorbusinesstypeforProfit,select_vendorbusinesstypeallawards,select_vendorbusinesstypecorprateentity,
                    select_vendorbusinesstypeManufactofgoods,select_contractvalue,select_contractduration,select_countryofprodservorigin)
        output_1 = list_name[0]
        #output_1.tostring().encode("Is Vendor Business Type - ", "")
        st.success('The business that will win the contract is{}'.format(output_1))

        output_2 = pd.DataFrame(list_name[1])
        #st.table(output)
        st.dataframe(output_2.style.highlight_max(axis=1))

    if __name__ == "__main__":
          main()

def contract_value_predict():
    import streamlit as st
    import html
    import torch
    import torch.nn as nn
    from torch.nn import LSTM
    from torch.utils.data import TensorDataset, DataLoader
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import requests, os
    import base64
    import streamlit.components.v1 as components
    from streamlit.components.v1 import html


    #sklearn
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.metrics import mean_squared_error as MSE
    
    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.75)), url("data:image/png;base64,%s");
        background-size:cover;
        background-repeat:no-repeat;
        position: absolute;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
        
    set_background("Images/GovernmentContract_Val.png") 
    st.write("# Predicting the Contract Value")
    st.markdown(
            """
            Before predicting the Contract Value, you can see the latest trends and visualizations by clicking on the link provided.
            """
            )
    def open_page(url):
        open_script= """
        <script type="text/javascript">
             window.open('%s', '_blank').focus();
        </script>
        """ % (url)
        html(open_script)

    st.button('Click to view tableau dashboard', on_click=open_page, args=('https://public.tableau.com/views/IDS560_dashboard_N/Story1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link',))
    
        
    st.markdown(
            """
                Let's now predict the Contract Value.
                Please fill out the fields on the left and click on the button below to see the output.
    
            """
            )
    st.button ("Predict the Contract Value")
    
    # #Sliders instead of the boxes
    # x1 = st.sidebar.slider("Contract Value Week1", min_value=0e1, max_value=1e10, value=1e8, step=1e2)
    # x2 = st.sidebar.slider("Contract Value Week2", min_value=0e1, max_value=1e10, value=2e8, step=1e2)
    # x3 = st.sidebar.slider("Contract Value Week3", min_value=0e1, max_value=1e10, value=3e8, step=1e2)
    # x4 = st.sidebar.slider("Contract Value Week4", min_value=0e1, max_value=1e10, value=4e8, step=1e2)
    # x5 = st.sidebar.slider("Contract Value Week5", min_value=0e1, max_value=1e10, value=3e8, step=1e2)

    # contract_type = st.sidebar.radio("Contract type",('Expensive','Medium','Cheap'))
    
    #CHANGE - Vojta
    contract_type = st.sidebar.radio("Contract type",('Expensive','Medium','Cheap'))

    if contract_type == 'Expensive':
      max_value = 1e11
      value = 1e10
    elif contract_type == 'Medium':
      max_value = 1e9
      value = 1e8
    elif contract_type == 'Cheap':
      max_value = 1e8
      value = 1e7
    
    #Sliders instead of the boxes
    x1 = st.sidebar.slider("Contract value 5 weeks ago", min_value=0e1, max_value=max_value, value=value, step=1e2)
    x2 = st.sidebar.slider("Contract value 4 weeks ago", min_value=0e1, max_value=max_value, value=value, step=1e2)
    x3 = st.sidebar.slider("Contract value 3 weeks ago", min_value=0e1, max_value=max_value, value=value, step=1e2)
    x4 = st.sidebar.slider("Contract value 2 weeks ago", min_value=0e1, max_value=max_value, value=value, step=1e2)
    x5 = st.sidebar.slider("Contract value last week", min_value=0e1, max_value=max_value, value=value, step=1e2)
    
    #Choosing the option
    print(contract_type)
    
    #Compiling into an INPUT
    input = [x1,x2,x3,x4,x5]
        
    #Reading the FILES
    #MODELS - with torch
    model_expensive = torch.load('Pickle/expensive_model.pth')
    model_medium = torch.load('Pickle/medium_model.pth')
    model_cheap = torch.load('Pickle/cheap_model.pth')

    #SCALERS
    with open('Pickle/epensive_scaler.pkl', 'rb') as f:
        expensive_scaler = pickle.load(f)
    with open('Pickle/medium_scaler.pkl', 'rb') as f:
        medium_scaler = pickle.load(f)
    with open('Pickle/cheap_scaler.pkl', 'rb') as f:
        cheap_scaler = pickle.load(f)
        
    def perform_prediction(input, model, scaler):
      '''Scale the input and compute the predicted value'''
      input_np = np.array(input)
      scaled_input = scaler.transform(input_np.reshape(-1,1))
      input_tensor = torch.from_numpy(scaled_input).float()
    
      predicted_y = model(input_tensor.unsqueeze(0))
      return scaled_input, predicted_y.detach().numpy() #X - input, y - prediction
    
    def print_the_prediction(input, model, scaler, title_name, y_xis_name):
      '''Uses the perform_prediction and prints it out on a plot'''
      scaled_input, predicted_y = perform_prediction(input, model, scaler)
      input_org = scaler.inverse_transform(scaled_input.reshape(-1,1))
      prediction_org = scaler.inverse_transform(predicted_y)
    
      # # PLotting in the scaled down version
      # fig_value, ax = plt.subplots()
      # ax.plot(scaled_input, label = 'Actual')
      # ax.plot([4,5], np.concatenate((scaled_input[-1].reshape(-1,1),predicted_y)), label = 'Predictions')
      # ax.set_title(title_name)
      # ax.set_ylabel(y_xis_name)
      # plt.legend()
      # plt.show()
      # st.pyplot(fig_value)
    
    
      # Origninal units
      fig_org, ax = plt.subplots()
      ax.plot(input_org, label = 'Actual')
      ax.plot([4,5], np.concatenate((input_org[-1].reshape(-1,1),prediction_org)), label = 'Predictions')
      ax.set_title(title_name)
      ax.set_ylabel(y_xis_name)
      ax.legend()
      st.pyplot(fig_org)
      # plt.show()
      return prediction_org
      
    #Body of the page

    if st.button ("Predict the Contract Value"):
        #Adjusting the choice of models and scalers made by users
      if contract_type == 'Expensive':
        model = model_expensive
        scaler = expensive_scaler
        title = 'Expensive'
      elif contract_type == 'Medium':
        model = model_medium
        scaler = medium_scaler
        title = 'Medium'
      elif contract_type == 'Cheap':
        model = model_cheap
        scaler = cheap_scaler
        title = 'Cheap'
    
    prediction = print_the_prediction(input, model, scaler, f'{title} Value', 'Contract value')
    st.write(f'The predicted value of the next week: {prediction}')
    
    def main():
        import streamlit as st
        import html
        import torch
        import torch.nn as nn
        from torch.nn import LSTM
        from torch.utils.data import TensorDataset, DataLoader
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import requests, os
        import base64
        import streamlit.components.v1 as components
        from streamlit.components.v1 import html


        #sklearn
        from sklearn.preprocessing import MinMaxScaler
        from sklearn.metrics import mean_squared_error as MSE
        ## The architecture of LSTM needed to be present for the imported models to run
        class LSTM(nn.Module):
          def __init__(self,input_size, hidden_size, num_stacked_layers):
            super().__init__()
            self.hidden_size = hidden_size
            self.num_stacked_layers = num_stacked_layers
            self.lstm = nn.LSTM(input_size = input_size,
                                hidden_size = hidden_size,
                                num_layers = num_stacked_layers,
                                batch_first = True)
            self.fc = nn.Linear(hidden_size,1)
    
          def forward(self,x):
        
            #initialize the states
            h0 = torch.zeros(self.num_stacked_layers, x.size(0),self.hidden_size)
            c0 = torch.zeros(self.num_stacked_layers, x.size(0),self.hidden_size)
            out, _ = self.lstm(x, (h0,c0))
            out = self.fc(out[:,-1,:]) ## out
            return out
        ##
    if __name__ == "__main__":
        main()

def contract_duration_predict():
    import pandas as pd
    import numpy as np
    import pickle
    import requests, os
    import base64
    import streamlit as st
    import streamlit.components.v1 as components
    from streamlit.components.v1 import html


    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.75)), url("data:image/png;base64,%s");
        background-size:cover;
        background-repeat:no-repeat;
        position: absolute;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
    set_background("Images/GovernmentContract_Dur.png")   

    def construct_sample_duration(input):

        # Load the serialized object from the pickle file
        with open('Pickle/label_encoder.pkl', 'rb') as file:
          label_encoders = pickle.load(file)

        X_test = np.zeros(20)
        X_test[0] = label_encoders['Contracting Agency ID'].transform([input[0]])
        X_test[1] = label_encoders['Domestic or Foreign Entity'].transform([input[5]])
        X_test[2] = label_encoders['Is Performance Based Service Acquisition'].transform([input[6]])
        X_test[3] = label_encoders['Type of Contract'].transform([input[1]])
        X_test[4] = label_encoders['NAICS Code'].transform([input[2][:2]])
        X_test[5] = label_encoders['Principal Place of Performance State Code'].transform([input[3]])
        X_test[6] = label_encoders['Principal Place of Performance Country Name'].transform([input[4]])
        X_test[7] = label_encoders['Country of Product or Service Origin'].transform([input[18]])
        X_test[8] = label_encoders['Extent Competed'].transform([input[7]])
        X_test[9] = label_encoders['Solicitation Procedures'].transform([input[8]])
        X_test[10] = label_encoders['Local Area Set Aside'].transform([input[9]])
        X_test[11] = label_encoders['Vendor Address State Name'].transform([input[10]])
        X_test[12] = label_encoders['Vendor Address Country Name'].transform([input[11]])
        X_test[13] = label_encoders['Labor Standards'].transform([input[12]])
        X_test[14] = label_encoders['Is Vendor Business Type - For Profit Organization'].transform([input[13]])
        X_test[15] = label_encoders['Is Vendor Business Type - All Awards'].transform([input[14]])
        X_test[16] = label_encoders['Is Vendor Business Type - Corporate Entity, Not Tax Exempt'].transform([input[15]])
        X_test[17] = label_encoders['Is Vendor Business Type - Manufacturer Of Goods'].transform([input[16]])
        X_test[18] = label_encoders['Business Type'].transform([input[19]])
        X_test[19] = label_encoders['Base and All Options Value (Total Contract Value)'].transform(np.array([input[17]]).reshape(-1, 1))

        return X_test

    def run_pred_duration (select_agencyid : str,select_contracttype : str,select_naicscode : str,select_pricipalplaceofperformancestate : str,
                       select_pricipalplaceofperformancecountry: str,select_entity: str,select_performancebasedservice: str,select_extentcompeted: str,
                       select_solicitationprocedures: str,select_localareasetaside: str,select_vendoraddresstatename: str,select_vendoraddresscountryname: str,
                       select_laborstandards: str,select_vendorbusinesstypeforProfit: str,select_vendorbusinesstypeallawards: str,select_vendorbusinesstypecorprateentity: str,
                       select_vendorbusinesstypeManufactofgoods: str,select_contractvalue: str,select_countryofprodservorigin: str,select_businesstype: str):

          #Generate prediction
      input = [select_agencyid,select_contracttype,select_naicscode,select_pricipalplaceofperformancestate,select_pricipalplaceofperformancecountry,
                          select_entity,select_performancebasedservice,select_extentcompeted,select_solicitationprocedures,select_localareasetaside,
                          select_vendoraddresstatename,select_vendoraddresscountryname,select_laborstandards,select_vendorbusinesstypeforProfit,
                          select_vendorbusinesstypeallawards,select_vendorbusinesstypecorprateentity,select_vendorbusinesstypeManufactofgoods,
                          select_contractvalue,select_countryofprodservorigin,select_businesstype]

      X_test = construct_sample_duration(input)

      # Load the serialized object from the pickle file -> change for duration model
      with open('Pickle/dur_xgb.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

      # Load the serialized object from the pickle file
      with open('Pickle/label_encoder.pkl', 'rb') as file:
        label_encoders = pickle.load(file)

      #Regression of the Duration - I think reshaping is not necessary
      prediction = loaded_model.predict(X_test.reshape(1, -1))

      Contract_Duration = label_encoders['Duration of Contract'].inverse_transform([prediction])
      return Contract_Duration

    st.write("# Predicting the Duration of contract")
    st.markdown(
        """
        Before predicting the Duration of the contract, you can see the latest trands and visualizations by clicking on the link provided.
        """
        )
    def open_page(url):
        open_script= """
        <script type="text/javascript">
             window.open('%s', '_blank').focus();
        </script>
        """ % (url)
        html(open_script)

    st.button('Click to view tableau dashboard', on_click=open_page, args=('https://public.tableau.com/views/IDS560_dashboard_N/Story1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link',))

    
    st.markdown(
        """
            Let's now predict the duration of the contract.
            Please fill out the fields on the left and click on the button below to see the output.

        """
        )

    #-- Set Duration of contract
    select_businesstype = st.sidebar.selectbox('What business type do you want to see?',
                                    ['Others',	'Is Vendor Business Type - Limited Liability Corporation',	'Is Vendor Business Type - Subchapter S Corporation',
                                     'Is Vendor Business Type - Self-Certified Small Disadvantaged Business',	'Is Vendor Business Type - Women-Owned Business',
                                     'Is Vendor Business Type - The AbilityOne Program',	'Is Vendor Business Type - Partnership or Limited Liability Partnership',
                                     'Is Vendor Business Type - Foreign Owned',	'Is Vendor Business Type - Veteran-Owned Business',
                                     'Is Vendor Business Type - Hispanic American Owned',	'Is Vendor Business Type - Contracts',
                                     'Is Vendor Business Type - 8A Program Participant',	'Is Vendor Business Type - Native American Owned',
                                     'Is Vendor Business Type - Sole Proprietorship',	'Is Vendor Business Type - Subcontinent Asian (Asian-Indian) American Owned',
                                     'Is Vendor Business Type - Black American Owned',	'Is Vendor Business Type - HUBZone Firm',
                                     'Is Vendor Business Type - Asian-Pacific American Owned',
                                     'Is Vendor Business Type - DoT Certified Disadvantaged Business Enterprise',
                                     'Is Vendor Business Type - Other Not For Profit Organization',	'Is Vendor Business Type - Other Minority-Owned'])

    select_agencyid = st.sidebar.text_input(label="Contracting Agency ID", placeholder="1406")

    select_contracttype = st.sidebar.selectbox('Contract Type',
                                        ['FIRM FIXED PRICE','TIME AND MATERIALS','LABOR HOURS','FIXED PRICE AWARD FEE','FIXED PRICE WITH ECONOMIC PRICE ADJUSTMENT','COST NO FEE','COST PLUS FIXED FEE','COST PLUS AWARD FEE','COST PLUS INCENTIVE FEE','FIXED PRICE INCENTIVE','FIXED PRICE LEVEL OF EFFORT','COST SHARING','FIXED PRICE REDETERMINATION'])

    select_naicscode = st.sidebar.text_input(label="NAICS Code", placeholder="622109")

    select_pricipalplaceofperformancestate = st.sidebar.selectbox('Principal place of performance state code', ['VA',	'DC',	'CA',	'MD',	'IN',	'FL',	'NY',	'MO',	'CO',	'AK',	'LA',	'ID',	'WY',	'SD',	'MT',	'OR',	'WA',	'VT',	'PA',	'NM',	'NJ',	'IL',	'MN',	'TX',	'WV',	'AL',	'PR',	'KY',	'SC',	'NC',	'OK',	'GA',	'AR',	'MS',	'NE',	'MI',	'OH',	'IA',	'DE',	'NH',	'KS',	'WI',	'AZ',	'TN',	'CT',	'MA',	'HI',	'UT',	'RI',	'ME',	'ND',	'NV',	'AS',	'UGANDA',	'GU',	'FRANCE',	'VI',	'VIETNAM',	'CANADA',	'JAPAN',	'UNITED KINGDOM',	'BAHRAIN',	'DJIBOUTI',	'SPAIN',	'ITALY',	'GREECE',	'SINGAPORE',	'SRI LANKA',	'BANGLADESH',	'SAMOA',	'PHILIPPINES',	'CAMBODIA',	'MICRONESIA, FEDERATED STATES OF',	'MONGOLIA',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'LAOS',	'MP',	'AUSTRALIA',	'CROATIA',	'ROMANIA',	'CUBA',	'INDIA',	'IRAQ',	'ANGOLA',	'AFGHANISTAN',	'ALGERIA',	'AZERBAIJAN',	'ALBANIA',	'CENTRAL AFRICAN REPUBLIC',	'HONDURAS',	'ISRAEL',	'THAILAND',	'KOREA, SOUTH',	'PERU',	'URUGUAY',	'JAMAICA',	'SOUTH SUDAN',	'BAHAMAS, THE',	'ERITREA',	'NAMIBIA',	'MOROCCO',	'GERMANY',	'SOMALIA',	'JORDAN',	'CAMEROON',	'POLAND',	'MOZAMBIQUE',	'SAUDI ARABIA',	'DOMINICAN REPUBLIC',	'LEBANON',	'CONGO (KINSHASA)',	'TURKEY',	'NEW ZEALAND',	'CONGO (BRAZZAVILLE)',	'TURKMENISTAN',	'GUYANA',	'PARAGUAY',	'CYPRUS',	'SUDAN',	'GUATEMALA',	'KENYA',	'ARGENTINA',	'SOUTH AFRICA',	'BOTSWANA',	'BELGIUM',	'BURMA',	'BRAZIL',	'BURUNDI',	'COLOMBIA',	'CHILE',	'CHINA',	'COSTA RICA',	'IRELAND',	'ECUADOR',	'EL SALVADOR',	'ETHIOPIA',	'CZECHIA',	'FIJI',	'AUSTRIA',	'SLOVENIA',	'UZBEKISTAN',	'SLOVAKIA',	'NORTH MACEDONIA',	'BULGARIA',	'KOSOVO',	'RWANDA',	'GEORGIA',	'KAZAKHSTAN',	'UKRAINE',	'SENEGAL',	'ARMENIA',	'NIGERIA',	'BELARUS',	'ESWATINI',	'MOLDOVA',	'LATVIA',	'NIGER',	'MONTENEGRO',	'BURKINA FASO',	'LESOTHO',	'LITHUANIA',	'EGYPT',	'GABON',	'CHAD',	'PANAMA',	'UNITED ARAB EMIRATES',	'LIBERIA',	'MALAWI',	'MAURITIUS',	'MAURITANIA',	'OMAN',	'CURACAO',	'PAKISTAN',	'PAPUA NEW GUINEA',	'SERBIA',	'TUNISIA',	'TIMOR-LESTE',	'SWITZERLAND',	'ICELAND',	'BOSNIA AND HERZEGOVINA',	'KUWAIT',	'UNITED STATES MINOR OUTLYING ISLANDS',	'GUANTANAMO BAY NAVAL BASE',	'MEXICO',	'GREENLAND',	'PORTUGAL',	'QATAR',	'SYRIA',	'ZIMBABWE',	'TANZANIA',	'GHANA',	'GUINEA',	'MALI',	'DENMARK',	'SWEDEN',	'NETHERLANDS',	'BENIN',	'CABO VERDE',	'SOLOMON ISLANDS'])
   
    select_pricipalplaceofperformancecountry = st.sidebar.selectbox('Principal place of performance country name',
                                        ['UNITED STATES',	'UGANDA',	'FRANCE',	'VIETNAM',	'CANADA',	'JAPAN',	'UNITED KINGDOM',	'BAHRAIN',	'DJIBOUTI',	'SPAIN',	'ITALY',	'GREECE',	'SINGAPORE',	'SRI LANKA',	'BANGLADESH',	'SAMOA',	'PHILIPPINES',	'CAMBODIA',	'MICRONESIA, FEDERATED STATES OF',	'MONGOLIA',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'LAOS',	'AUSTRALIA',	'CROATIA',	'ROMANIA',	'CUBA',	'INDIA',	'IRAQ',	'ANGOLA',	'AFGHANISTAN',	'ALGERIA',	'AZERBAIJAN',	'ALBANIA',	'CENTRAL AFRICAN REPUBLIC',	'HONDURAS',	'ISRAEL',	'THAILAND',	'KOREA, SOUTH',	'PERU',	'URUGUAY',	'JAMAICA',	'SOUTH SUDAN',	'BAHAMAS, THE',	'ERITREA',	'NAMIBIA',	'MOROCCO',	'GERMANY',	'SOMALIA',	'JORDAN',	'CAMEROON',	'POLAND',	'MOZAMBIQUE',	'SAUDI ARABIA',	'DOMINICAN REPUBLIC',	'LEBANON',	'CONGO (KINSHASA)',	'TURKEY',	'NEW ZEALAND',	'CONGO (BRAZZAVILLE)',	'TURKMENISTAN',	'GUYANA',	'PARAGUAY',	'CYPRUS',	'SUDAN',	'GUATEMALA',	'KENYA',	'ARGENTINA',	'SOUTH AFRICA',	'BOTSWANA',	'BELGIUM',	'BURMA',	'BRAZIL',	'BURUNDI',	'COLOMBIA',	'CHILE',	'CHINA',	'COSTA RICA',	'IRELAND',	'ECUADOR',	'EL SALVADOR',	'ETHIOPIA',	'CZECHIA',	'FIJI',	'AUSTRIA',	'SLOVENIA',	'UZBEKISTAN',	'SLOVAKIA',	'NORTH MACEDONIA',	'BULGARIA',	'KOSOVO',	'RWANDA',	'GEORGIA',	'KAZAKHSTAN',	'UKRAINE',	'SENEGAL',	'ARMENIA',	'NIGERIA',	'BELARUS',	'ESWATINI',	'MOLDOVA',	'LATVIA',	'NIGER',	'MONTENEGRO',	'BURKINA FASO',	'LESOTHO',	'LITHUANIA',	'EGYPT',	'GABON',	'CHAD',	'PANAMA',	'UNITED ARAB EMIRATES',	'LIBERIA',	'MALAWI',	'MAURITIUS',	'MAURITANIA',	'OMAN',	'CURACAO',	'PAKISTAN',	'PAPUA NEW GUINEA',	'SERBIA',	'TUNISIA',	'TIMOR-LESTE',	'SWITZERLAND',	'ICELAND',	'BOSNIA AND HERZEGOVINA',	'KUWAIT',	'UNITED STATES MINOR OUTLYING ISLANDS',	'GUANTANAMO BAY NAVAL BASE',	'MEXICO',	'GREENLAND',	'PORTUGAL',	'QATAR',	'SYRIA',	'ZIMBABWE',	'TANZANIA',	'GHANA',	'GUINEA',	'MALI',	'DENMARK',	'SWEDEN',	'NETHERLANDS',	'BENIN',	'CABO VERDE',	'SOLOMON ISLANDS'])

    select_entity = st.sidebar.selectbox("Domestic or Foreign Entity",['U.S. OWNED BUSINESS','OTHER U.S. ENTITY (E.G. GOVERNMENT)','FOREIGN-OWNED BUSINESS INCORPORATED IN THE U.S.','FOREIGN-OWNED BUSINESS NOT INCORPORATED IN THE U.S.','OTHER FOREIGN ENTITY (E.G. FOREIGN GOVERNMENT)'])

    select_performancebasedservice = st.sidebar.radio("Performance Based Service Acquisition",('NO - SERVICE WHERE PBA IS NOT USED.','YES - SERVICE WHERE PBA IS USED.','NOT APPLICABLE'))

    select_extentcompeted = st.sidebar.selectbox('Extent Competed',
                                        ['FULL AND OPEN COMPETITION','NOT COMPETED UNDER SAP','FULL AND OPEN COMPETITION AFTER EXCLUSION OF SOURCES','NOT COMPETED','COMPETED UNDER SAP','NOT AVAILABLE FOR COMPETITION'])

    select_solicitationprocedures = st.sidebar.selectbox('Solicitation Procedures',
                                        ['SUBJECT TO MULTIPLE AWARD FAIR OPPORTUNITY','SIMPLIFIED ACQUISITION','NEGOTIATED PROPOSAL/QUOTE','ONLY ONE SOURCE','ALTERNATIVE SOURCES','SEALED BID','ARCHITECT-ENGINEER FAR 6.102','BASIC RESEARCH','TWO STEP'])

    select_localareasetaside = st.sidebar.radio("Local Area Set Aside",('YES','NO'))

    select_vendoraddresstatename = st.sidebar.selectbox('Vendor Address State',
                                        ['VIRGINIA',	'MARYLAND',	'FLORIDA',	'RHODE ISLAND',	'CALIFORNIA',	'INDIANA',	'NEW YORK',	'NORTH CAROLINA',	'MINNESOTA',	'MISSOURI',	'ALASKA',	'TEXAS',	'PENNSYLVANIA',	'MISSISSIPPI',	'IDAHO',	'WYOMING',	'OREGON',	'DISTRICT OF COLUMBIA',	'MONTANA',	'WASHINGTON',	'MASSACHUSETTS',	'NEW JERSEY',	'ILLINOIS',	'WEST VIRGINIA',	'COLORADO',	'OHIO',	'ALABAMA',	'KENTUCKY',	'GEORGIA',	'OKLAHOMA',	'LOUISIANA',	'KANSAS',	'NEBRASKA',	'SOUTH CAROLINA',	'NEVADA',	'NEW MEXICO',	'WISCONSIN',	'SOUTH DAKOTA',	'ARKANSAS',	'ARIZONA',	'MICHIGAN',	'PUERTO RICO',	'CONNECTICUT',	'HAWAII',	'TENNESSEE',	'UTAH',	'VERMONT',	'IOWA',	'NEW HAMPSHIRE',	'MAINE',	'DELAWARE',	'NORTH DAKOTA',	'VIRGIN ISLANDS OF THE U.S.',	'GUAM',	'AMERICAN SAMOA',	'NORTHERN MARIANA ISLANDS',	'CANADA',	'FRANCE',	'UNITED KINGDOM',	'JAPAN',	'ROMANIA',	'SPAIN',	'ITALY',	'SINGAPORE',	'SRI LANKA',	'NEW ZEALAND',	'IRAQ',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'PHILIPPINES',	'VIETNAM',	'CROATIA',	'GREECE',	'UNITED ARAB EMIRATES',	'INDIA',	'BAHRAIN',	'BELGIUM',	'COLOMBIA',	'CAMBODIA',	'CONGO (KINSHASA)',	'COSTA RICA',	'FIJI',	'SLOVENIA',	'KENYA',	'UZBEKISTAN',	'MOROCCO',	'SLOVAKIA',	'BULGARIA',	'ALBANIA',	'KAZAKHSTAN',	'AZERBAIJAN',	'UKRAINE',	'SENEGAL',	'SOUTH AFRICA',	'THAILAND',	'NIGERIA',	'ARMENIA',	'LITHUANIA',	'BURUNDI',	'UGANDA',	'MOLDOVA',	'ALGERIA',	'ESTONIA',	'LATVIA',	'MOZAMBIQUE',	'RWANDA',	'CYPRUS',	'GABON',	'MONTENEGRO',	'NETHERLANDS',	'KOREA, SOUTH',	'NIGER',	'PANAMA',	'SERBIA',	'SOUTH SUDAN',	'SWITZERLAND',	'GERMANY',	'BOTSWANA',	'ICELAND',	'SAUDI ARABIA',	'POLAND',	'NORTH MACEDONIA',	'KOSOVO',	'BOSNIA AND HERZEGOVINA',	'PERU',	'KUWAIT',	'PORTUGAL',	'DENMARK',	'QATAR',	'GHANA',	'ISRAEL',	'MALI',	'SWEDEN',	'AUSTRALIA',	'AUSTRIA',	'JORDAN'])

    select_vendoraddresscountryname = st.sidebar.selectbox('Vendor address country name',
                                        ['UNITED STATES',	'CANADA',	'FRANCE',	'UNITED KINGDOM',	'JAPAN',	'ROMANIA',	'GUAM',	'SPAIN',	'ITALY',	'SINGAPORE',	'SRI LANKA',	'NEW ZEALAND',	'IRAQ',	'MALAYSIA',	'NEPAL',	'INDONESIA',	'PHILIPPINES',	'VIETNAM',	'CROATIA',	'GREECE',	'UNITED ARAB EMIRATES',	'INDIA',	'BAHRAIN',	'BELGIUM',	'COLOMBIA',	'CAMBODIA',	'CONGO (KINSHASA)',	'COSTA RICA',	'FIJI',	'SLOVENIA',	'KENYA',	'UZBEKISTAN',	'MOROCCO',	'SLOVAKIA',	'BULGARIA',	'ALBANIA',	'GEORGIA',	'KAZAKHSTAN',	'AZERBAIJAN',	'UKRAINE',	'SENEGAL',	'SOUTH AFRICA',	'THAILAND',	'NIGERIA',	'ARMENIA',	'LITHUANIA',	'BURUNDI',	'UGANDA',	'MOLDOVA',	'ALGERIA',	'ESTONIA',	'LATVIA',	'MOZAMBIQUE',	'RWANDA',	'CYPRUS',	'GABON',	'MONTENEGRO',	'NETHERLANDS',	'KOREA, SOUTH',	'NIGER',	'PANAMA',	'SERBIA',	'SOUTH SUDAN',	'SWITZERLAND',	'GERMANY',	'BOTSWANA',	'ICELAND',	'SAUDI ARABIA',	'POLAND',	'NORTH MACEDONIA',	'KOSOVO',	'BOSNIA AND HERZEGOVINA',	'PERU',	'KUWAIT',	'PORTUGAL',	'DENMARK',	'QATAR',	'GHANA',	'ISRAEL',	'MALI',	'SWEDEN',	'AUSTRALIA',	'AUSTRIA',	'JORDAN'])


    select_laborstandards = st.sidebar.radio("Labor Standards",('YES','NO','NOT APPLICABLE'))

    select_vendorbusinesstypeforProfit = st.sidebar.radio("Is Vendor Business type - For Profit Organisation",('YES','NO'))

    select_vendorbusinesstypeallawards = st.sidebar.radio("Is Vendor Business type - All Awards ",('YES','NO'))

    select_vendorbusinesstypecorprateentity = st.sidebar.radio("Is Vendor Business type - Corporate Entity, Not tax Exempt",('YES','NO'))

    select_vendorbusinesstypeManufactofgoods = st.sidebar.radio("Is Vendor Business type - Manufacturer of Goods",('YES','NO'))

    select_contractvalue = st.sidebar.text_input(label="Total Contract Value", placeholder="$25,000,000")

    select_countryofprodservorigin = st.sidebar.selectbox('Country of Product or Service Origin',
                                        ['UNITED STATES','INDIA','CANADA','MEXICO'])

   
    def main():
      import pickle
      import pandas as pd
      import os
      import seaborn as sns
      import matplotlib.pyplot as plt
      import numpy as np
      from sklearn import preprocessing
      from sklearn.preprocessing import MinMaxScaler
      from sklearn.model_selection import train_test_split
      import pickle
      from sklearn.metrics import confusion_matrix
      from sklearn import metrics
      from sklearn.model_selection import cross_validate
      from sklearn.tree import DecisionTreeClassifier
      from sklearn.model_selection import GridSearchCV, cross_validate
      from sklearn.tree import DecisionTreeClassifier
      from sklearn.ensemble import RandomForestClassifier
      from sklearn.model_selection import RandomizedSearchCV
      from sklearn.ensemble import RandomForestClassifier
      from sklearn.metrics import accuracy_score, f1_score
      import numpy as np
      from sklearn.inspection import permutation_importance
      from sklearn.neighbors import KNeighborsClassifier
      from sklearn.neighbors import KNeighborsClassifier
      from sklearn.model_selection import RandomizedSearchCV, cross_validate
      from sklearn.metrics import make_scorer, accuracy_score, f1_score
      from sklearn import linear_model
      from sklearn.metrics import r2_score
      from sklearn.linear_model import Ridge
      from sklearn.model_selection import GridSearchCV
      from sklearn.linear_model import Lasso
      import xgboost as xg
      from sklearn.metrics import mean_squared_error as MSE
      from sklearn.metrics import accuracy_score
      from sklearn.linear_model import Ridge
      
        
      # Load the serialized object from the pickle file
      with open('Pickle/dur_xgb.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

      # Load the serialized object from the pickle file
      with open('Pickle/label_encoder.pkl', 'rb') as file:
        label_encoders = pickle.load(file)

    #html_temp = "<div class='tableauPlaceholder' id='viz1710733360364' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ID&#47;IDS_560_dashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IDS_560_dashboard&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ID&#47;IDS_560_dashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1710733360364');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1620px';vizElement.style.maxWidth='1720px';vizElement.style.width='100%';vizElement.style.minHeight='818px';vizElement.style.maxHeight='910px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1620px';vizElement.style.maxWidth='1720px';vizElement.style.width='100%';vizElement.style.minHeight='818px';vizElement.style.maxHeight='910px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1250px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    #components.html(html_temp)

    if st.button ("Predict the Duration of the contract"):
      output = run_pred_duration(select_agencyid,select_contracttype,select_naicscode,select_pricipalplaceofperformancestate,
                select_pricipalplaceofperformancecountry,select_entity,select_performancebasedservice,select_extentcompeted,select_solicitationprocedures,
                select_localareasetaside,select_vendoraddresstatename,select_vendoraddresscountryname,select_laborstandards,
                select_vendorbusinesstypeforProfit,select_vendorbusinesstypeallawards,select_vendorbusinesstypecorprateentity,
                select_vendorbusinesstypeManufactofgoods,select_contractvalue,select_countryofprodservorigin,select_businesstype)

      st.success('The duration of the contract is {} days'.format(int(output)))
      # #st.table(output)
      # st.dataframe(output.style.highlight_max(axis=1))

    if __name__ == "__main__":
       main()

page_names_to_funcs = {
    "Home Page": intro,
    "Predict Business Type": business_type_predict,
    "Predict Contract Value": contract_value_predict,
    "Predict Contract Duration": contract_duration_predict
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
