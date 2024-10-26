chatName="//div[@id='main']//div[@class='_amie']//span[@dir='auto']"
#===================================================================================================
chatPresent="//div[contains(@role,'listitem')]"
#===================================================================================================
imgs="//div[@role='application']//span[text()='TODAY']//following::img[@src[contains(., 'blob:https://web.whatsapp')]]"#imgs all of img with out gifs for persian languge 
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
text="//div[@role='application']//span[text()='TODAY']//following::div/div[contains(@class,'copyable-text')]/div/span/span[@class and string-length(text()) > 0]"