chatName="//div[@id='main']//div[@class='_amie']//span[@dir='auto']"
#===================================================================================================
chatPresent="//div[contains(@role,'listitem')]"
#===================================================================================================
imgs="//div[@role='application']//span[text()='TODAY']//following::img[contains(@src, 'blob:https://web.whatsapp.com/') and not(ancestor::div[contains(@data-id, 'album')])]"#imgs all of img with out gifs for persian languge 
#===================================================================================================
singleImgP="//div[@role='button' and @title='دانلود']"

#===================================================================================================
singleImgE="//div[@role='button' and @title='Download']"
#===================================================================================================
gropImg="//div[contains(@class,'_ajv6 x1y1aw1k x1sxyh0 xwib8y2 xurb0ha') and contains(@tabindex,'0')and contains(@title,'Menu')]"#ineed to find the first found thing not all them
#===================================================================================================
gropImgP2="//div[contains(@class,'_aj-z _aj-t _alxo') and @style and @aria-label='Download' ]"#its xpath for download button 
#===================================================================================================
Gmenu='(//div[contains(@class,"_ajv6 x1y1aw1k x1sxyh0 xwib8y2 xurb0ha")]//span[@data-icon="menu"])[1]'
#===================================================================================================
GmenuD="//div[contains(@class,'x10l6tqk x13vifvy xds687c x1ey2m1c x17qophe')and @tabindex='-1']//following::span[@class]//following::div[contains(@tabindex,'-1')]//ul/li[3]//div[contains(.,'Download')]"
#===================================================================================================
#===================================================================================================
readmore="//div[@role='application']//span[text()='TODAY']//following::div[contains(@class,'read-more-button')]"
#===================================================================================================

downloadButton="//div//span[contains(@data-icon,'download')]"
groptxt="//div[@role='application']//span[text()='TODAY']//following::div[contains(@class,'copyable-text')]"
#===================================================================================================
downloadButtonLoad="(//div[contains(@class,'x6s0dn4 x7o08j2 x78zum5 x5yr21d xl56j7k x17qophe x10l6tqk x13vifvy xh8yej3 x11uqc5h')]) //button"
#===================================================================================================
nextButton="//div [contains(@class,'x78zum5 x6s0dn4 xl56j7k x3x2bpi xwvwv9b xexx8yu x4uap5 x18d9i69 xkhd6sd x1f6kntn xk50ysn x7o08j2 xtvhhri x14yjl9h xudhj91 x18nykt9 xww2gxu xu306ak x12s1jxh xkdsq27 xwwtwea x1gfkgh9 x10l6tqk x8jeoy8 xyw6214 x160vmok x1sr6hwe')]/span "
#===================================================================================================
downloadMenu="(//span[contains(@class,'') and contains(@data-icon,'menu')])[1]"
#===================================================================================================
textBar="((//div[contains(@class,'x1n2onr6 xh8yej3 lexical-rich-text-input')])[2]/div)[1]"
downloadTab="//li/div[contains(@aria-label,'Download')]"
lenOfImgs="//p/span[contains(@class,'_alhf _ao3e')]"
albumImg="//div[@role='application']//span[text()='TODAY']//following::div[contains(@role,'row')]/div[@data-id[contains(.,'album')]]//div[contains(@style,'grid-area: 1 / 1 / 2 / 2;')]"
today="//div[@role='application']//span[text()='TODAY']"