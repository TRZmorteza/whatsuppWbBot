unreadfollow="//div[contains(@class,'focusable-list-item')]//span[contains(text(),'unread')]"
img="//img[@draggable='true'][contains(@src,'blob:https://web')]"
txt="//span[contains(@class,'selectable-text copyable-text')]//span"



escape_button="//button[contains(@role,'button')][contains(@title,'Close')]"
download_button="//button[contains(@role,'button')][contains(@title,'Download')]"
chatname="//header//div[contains(@role, 'button')]//span[contains(@dir,'auto')]"
unRead="//div[contains(@role,'listitem')]//following::span[contains(@aria-label,'unread message')]"
unread_imgs="//div[contains(@class,'focusable-list-item')]//span[contains(text(),'unread')]/following::img[@draggable='true'][contains(@src,'blob:https://web')]"
unread_texts="//div[contains(@class,'focusable-list-item')]//span[contains(text(),'unread')]::span[contains(@class,'selectable-text copyable-text')]/span"