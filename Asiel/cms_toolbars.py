from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER,LANGUAGE_MENU_IDENTIFIER,PAGE_MENU_IDENTIFIER,PAGE_MENU_ADD_IDENTIFIER 
from cms.toolbar.items import Menu,ModalButton
from djangocms_blog.cms_wizards import PostWizard
from cms.wizards.wizard_pool import wizard_pool
from cms.wizards.wizard_base import Wizard

@toolbar_pool.register
class MyBarToolbar(CMSToolbar):
    def populate(self):
        
        
        #admin_menu.disabled=True
      
        #print(self.toolbar.find_items(Menu, name="Local")[0].item.name)
        '''
        language_menu = self.toolbar.get_menu(LANGUAGE_MENU_IDENTIFIER )
        language_menu.disabled=True
        print(language_menu)

        page = self.toolbar.get_menu(PAGE_MENU_IDENTIFIER )
        page.disabled=True
        print(page)
        '''    
   
        #eliminando el wizzard
        for wizard in wizard_pool.get_entries(): 
            if wizard.title == "New Article":
                wizard_pool.unregister(wizard)

 






        