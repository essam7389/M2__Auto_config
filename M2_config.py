
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class nanocfg:

    def __init__(self, master ):
        
        self.master = master
        
        #header image
        self.photo = PhotoImage(file = "bg3.png")
        self.photoimage = self.photo.subsample(1, 1)# Resizing image to fit on button
        self.labelheader = ttk.Label(master, image = self.photoimage, compound = RIGHT )
        self.labelheader.grid(row= 0 ,sticky=W+E,  columnspan=3)

        #type of device fram
        self.typ_Frame = ttk.Frame(master)
        self.typ_Frame.grid(row= 1, column= 1 , padx= 2, pady= 2)
        self.typ_Frame.configure(borderwidth= 1)

        
        self.Chrome = IntVar()
        self.Chrome_Button = ttk.Checkbutton(self.typ_Frame, variable = self.Chrome,\
                                     text="Chrome   ", onvalue = 1, offvalue = 0)
        self.Chrome_Button.grid(row= 2 , column= 0 ,padx= 0, pady= 0)
        
        
        self.Firefox = IntVar()
        self.Firefox_Button = ttk.Checkbutton(self.typ_Frame, variable = self.Firefox,\
                                     text="Firefox   ", onvalue = 1, offvalue = 0)
        self.Firefox_Button.grid(row= 2 , column= 2 ,padx= 0, pady= 0)


        self.M2N = IntVar()
        self.m2_nano = ttk.Checkbutton(self.typ_Frame, variable = self.M2N,\
                                     text="M2_Nano", onvalue = 1, offvalue = 0)
        self.m2_nano.grid(row= 3 , column= 0 ,padx= 1, pady= 1)
        
        
        self.M2P = IntVar()
        self.m2_POW = ttk.Checkbutton(self.typ_Frame, variable = self.M2P,\
                                     text="M2_PowerBeam ", onvalue = 1, offvalue = 0)
        self.m2_POW.grid(row= 3 , column= 1 ,padx= 1, pady= 1)

        self.M2L = IntVar()
        self.m2_Loco = ttk.Checkbutton(self.typ_Frame, variable = self.M2L,\
                                     text="M2_Loco ", onvalue = 1, offvalue = 0)
        self.m2_Loco.grid(row= 3 , column= 2 ,padx= 1, pady= 1)
        
        #Parameters frame
        self.action_LabelFrame = ttk.LabelFrame(master)
        self.action_LabelFrame.grid(row= 3, column= 1 , padx= 2, pady= 2)
        self.action_LabelFrame.configure(borderwidth= 1)

        #SSID
        self.labelSSID = ttk.Label(self.action_LabelFrame, text=u"SSID اسم البث")
        self.labelSSID.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelSSID.grid(row= 2 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.entSSID = ttk.Entry(self.action_LabelFrame)
        self.entSSID.grid(row= 2 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.entSSID.insert(END,'Yemen_Net(11)')
        self.entSSID.configure(width="35",font=("Arial", 13))

        #Chanel
        self.labelchnl = ttk.Label(self.action_LabelFrame, text=u"القناة")
        self.labelchnl.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelchnl.grid(row= 3 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.chnl = IntVar()
        self.cboxchnl = ttk.Combobox(self.action_LabelFrame, textvariable = self.chnl)
        self.cboxchnl.set('2412')
        self.cboxchnl.grid(row= 3 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.cboxchnl.configure(width="33", values = ('2412','2417','2422','2427','2432','2437','2442','2447','2452','2457','2462'),font=("Arial", 13))

        # ip and mask and gatway
        self.labelip = ttk.Label(self.action_LabelFrame, text=u"  ip عنوان")
        self.labelip.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelip.grid(row= 4 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.entip = ttk.Entry(self.action_LabelFrame)
        self.entip.grid(row= 4 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.entip.insert(END,'177.88.1.11')
        self.entip.configure(width="35",font=("Arial", 13))

        self.labelmsk = ttk.Label(self.action_LabelFrame, text=u"قناع الشبكة")
        self.labelmsk.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelmsk.grid(row= 5 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.entmsk = ttk.Entry(self.action_LabelFrame)
        self.entmsk.grid(row= 5 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.entmsk.insert(END,'255.255.0.0')
        self.entmsk.configure(width="35",font=("Arial", 13))

        self.labelgtwy = ttk.Label(self.action_LabelFrame, text=u"البوابة الافتراضية")
        self.labelgtwy.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelgtwy.grid(row= 6 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.entgtwy = ttk.Entry(self.action_LabelFrame)
        self.entgtwy.grid(row= 6 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.entgtwy.insert(END,'177.88.0.1')
        self.entgtwy.configure(width="35",font=("Arial", 13))

        #device name and username and pass
        self.labelname = ttk.Label(self.action_LabelFrame, text=u"اسم الجهاز")
        self.labelname.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelname.grid(row= 7 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.entname = ttk.Entry(self.action_LabelFrame)
        self.entname.grid(row= 7 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.entname.insert(END,'M2(11)')
        self.entname.configure(width="35",font=("Arial", 13))

        self.labelusrnm = ttk.Label(self.action_LabelFrame, text=u"اسم المســتخدم")
        self.labelusrnm.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelusrnm.grid(row= 8 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.entusrnm = ttk.Entry(self.action_LabelFrame)
        self.entusrnm.grid(row= 8 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.entusrnm.insert(END,'admin')
        self.entusrnm.configure(width="35",font=("Arial ", 13))


        self.labelpass = ttk.Label(self.action_LabelFrame, text=u"كلمة المرور")
        self.labelpass.config(font=("Arial Bold", 15), borderwidth= 0)
        self.labelpass.grid(row= 9 , column= 1 , sticky='e', padx= 5, pady= 2)

        self.entpass = ttk.Entry(self.action_LabelFrame)
        self.entpass.grid(row= 9 , column= 0 , sticky='w', padx= 5, pady= 2)
        self.entpass.insert(END,'')
        self.entpass.configure(width="35" , show = '*', font=("Arial", 13))

    
        self.btnConn = Button(master, text=u"تنفيذ الاعدادات", command = self.Action, bg = '#34BCFC')
        self.btnConn.grid(row=10, column=1)
        self.btnConn.configure(width="39", font=("Arial Bold", 15))

        self.labelheader = ttk.Label(master,text=u"برمجة م.عصام عميران" )
        self.labelheader.config(width="4", font=("Arial Bold", 12), borderwidth= 1)
        self.labelheader.grid(row= 11 ,sticky=W+E,  columnspan=3)
                          
#--------------------------------------------------------------------------------------------------------------------------
#Take Action
    def Action(self):
        chrome = self.Chrome.get()
        firefox = self.Firefox.get()
        

        if chrome == 1:
            options = Options()
            options.add_argument('--allow-running-insecure-content')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--disable-extensions")
            options.add_argument('--lang=en-us')
            browser=webdriver.Chrome(options=options)
            browser.implicitly_wait(10)
            browser.maximize_window()
        elif firefox ==1 :
            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True
            browser = webdriver.Firefox(firefox_profile=profile)
            browser.implicitly_wait(5)
            browser.maximize_window()

        else:
            msgs = messagebox.showerror(u"خطأ",u" اختر المتصفح ")
            
        
#---------------------------------------------------------------------------------------------------------
#login page  
        browser.get("http://192.168.1.20/login.cgi?uri=/")

        try:
            username_field = browser.find_element_by_name("username")
            password_field = browser.find_element_by_name("password")
            username_field.send_keys("ubnt")
            password_field.send_keys("ubnt")
            browser.find_element_by_css_selector("#country [value='840']").click()
            browser.find_element_by_id("agreed").click()
            browser.find_element_by_xpath("//input[@value='Login']").click()


        except:
            browser.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/input").click()
#-------------------------------------------------------------------------------
#system tab
        device_name = self.entname.get()
        usrname = self.entusrnm.get()
        password = self.entpass.get()

        browser.get("http://192.168.1.20/system.cgi")
        time.sleep(2)
        chkbox = browser.find_element_by_id("update_status").click()
        Device_Name = browser.find_element_by_id("hostname")
        Device_Name.clear()
        Device_Name.send_keys(device_name)
        username_chng = browser.find_element_by_name("adminname")
        username_chng.clear()
        username_chng.send_keys(usrname)
        pass_chng_trig= browser.find_element_by_id("admin_passwd_trigger").click()
        oldpass_field = browser.find_element_by_name("OldPassword")
        newpass_field = browser.find_element_by_name("NewPassword")
        newpass2_field = browser.find_element_by_name("NewPassword2")
        oldpass_field.send_keys("ubnt")
        newpass_field.send_keys(password)
        newpass2_field.send_keys(password)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        try:
            browser.find_element_by_xpath("//*[@id='hide-warning']").click()
        except:
            pass
        chng_button = browser.find_element_by_id("system_change").click()

#----------------------------------------------------------------------------------------------------------------------------
#services tab
        browser.get("http://192.168.1.20/services.cgi")
        browser.find_element_by_id("https_status").click()
        browser.find_element_by_xpath("//input [@value='Change']").click()

#-------------------------------------------------------------------------------
#Advanced tab
        browser.get("http://192.168.1.20/advanced.cgi")
        browser.find_element_by_id("eirp_status").click()
        browser.find_element_by_xpath("//input [@value='Change']").click()
        
#-------------------------------------------------------------------------------
#Network
        new_ip = self.entip.get()
        new_msk = self.entmsk.get()
        new_gtwy = self.entgtwy.get()
        
        browser.get("http://192.168.1.20/network.cgi")
        wait_2 = WebDriverWait(browser, 10)
        mngmnt_ip = wait_2.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mgmtIpAddr")))
        mngmnt_ip = browser.find_element_by_id("mgmtIpAddr")
        mngmnt_ip.clear()
        mngmnt_ip.send_keys(new_ip)
        mngmnt_Nmsk = browser.find_element_by_id("mgmtIpNetmask")
        mngmnt_Nmsk.clear()
        mngmnt_Nmsk.send_keys(new_msk)
        mngmnt_Gtwy = browser.find_element_by_id("mgmtGateway")
        mngmnt_Gtwy.clear()
        mngmnt_Gtwy.send_keys(new_gtwy)
        mngmnt_Dns1 = browser.find_element_by_id("mgmtDns1")
        mngmnt_Dns1.send_keys(new_gtwy)
        mngmnt_Dns2 = browser.find_element_by_id("mgmtDns2")
        mngmnt_Dns2.send_keys(new_gtwy)
        browser.find_element_by_xpath("//input[@value='Change']").click()

#-----------------------------------------------------------------------------------------------------------------------------#
#open Wireless menue

        
        SSID = self.entSSID.get()
        chanel = str(self.cboxchnl.get())
        M2N = self.M2N.get()
        M2P = self.M2P.get()
        M2L = self.M2L.get()
        browser.get("http://192.168.1.20/ubnt.cgi")
        try:
            browser.get("http://192.168.1.20/link.cgi")
        except:
            pass
        browser.get("http://192.168.1.20/link.cgi")    
        browser.find_element_by_css_selector("#wmode [value='ap']").click() 
        browser.find_element_by_id("wds_chkbox").click()
        SSID_field = browser.find_element_by_id("essid")
        SSID_field.clear()
        SSID_field.send_keys(SSID)
        browser.find_element_by_css_selector("#chanbw_select [value='20']").click()
        browser.find_element_by_css_selector("#chan_freq [value="+"'"+chanel+"'"+"]").click()
        browser.find_element_by_id("obey_regulatory_checkbox").click()
        Txpower_field = browser.find_element_by_id("txpower")
        Txpower_field.clear()
        if M2N == 1:
            Txpower_field.send_keys("28")
        elif M2P == 1:
            Txpower_field.send_keys("28")
        elif M2L == 1:
            Txpower_field.send_keys("23")
                
        browser.find_element_by_xpath("//input[@value='Change']").click()

#------------------------------------------------------------------------------------------------------------------------------#
#AirMax
        browser.get("http://192.168.1.20/ubnt.cgi")
        browser.find_element_by_id("polling").click()
        browser.find_element_by_xpath("//input [@value='Change']").click()

#-------------------------------------------------------------------------------------------------------------------------------#
#Apply the changes
        browser.find_element_by_xpath("//input[@value='Apply']").click()

#-------------------------------------------------------------------------------------------------------------------------------#            

root = Tk()          # we create our application's main (root) window widget.
app = nanocfg(root)   # call the class
root.title("M2_config V1.1")
root.iconbitmap("u.ico")
root.geometry('')
root.mainloop()      # Main event loop
        
