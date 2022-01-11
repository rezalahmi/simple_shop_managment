
import shopWindow


class shopControl:

    def __init__(self):
        pass

    def startShop(self):
        myshop = shopWindow.shopView()
        model = shop_db.shopModel()
        model.connection()

        myshop.showWindow()