from PyQt6.QtWidgets import *
from gui import *
from gui2 import *
import re

cart = {}
selected_items = []
keys = cart.keys()


class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        """sets up the main window GUI with initial parameters"""
        super().__init__()
        self.setupUi(self)
        self.label_select_type.hide()
        self.dropdown_list.hide()
        self.button_select.hide()
        self.frame_option1.hide()
        self.frame_option2.hide()
        self.frame_option3.hide()
        self.frame_option4.hide()
        self.button_add.hide()
        self.label_pretax_total.hide()
        self.button_checkout.hide()
        self.dropdown_list.addItems(['Produce', 'Frozen Fruits', 'Bread', 'Meats', 'Chips', 'Snacks'])
        self.button_enter.clicked.connect(lambda: self.enter_store())
        self.dropdown_quantity1.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.dropdown_quantity2.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.dropdown_quantity3.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.dropdown_quantity4.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.button_select.clicked.connect(lambda: self.select_groceries())
        self.button_add.clicked.connect(lambda: self.add_to_cart())
        self.button_checkout.clicked.connect(lambda: self.checkout())
        self.total = 0

    def enter_store(self) -> None:
        """enters V.S. Grocery. Displays grocery options"""
        self.label_select_type.show()
        self.dropdown_list.show()
        self.button_select.show()
        self.button_enter.hide()
        self.label_welcome.move(70, 50)

    def select_groceries(self) -> None:
        """displays the grocery options from a selected group"""
        self.button_add.show()
        self.label_pretax_total.show()
        self.button_checkout.show()

        self.radioButton_option1.setChecked(False)
        self.radioButton_option2.setChecked(False)
        self.radioButton_option3.setChecked(False)
        self.radioButton_option4.setChecked(False)

        self.dropdown_quantity1.setCurrentIndex(0)
        self.dropdown_quantity2.setCurrentIndex(0)
        self.dropdown_quantity3.setCurrentIndex(0)
        self.dropdown_quantity4.setCurrentIndex(0)

        if self.dropdown_list.currentIndex() == 0:
            self.frame_option1.show()
            self.radioButton_option1.setText('Tomatoes')
            self.label_price1.show()
            self.label_price1.setText('$0.98/ea')
            self.frame_option2.show()
            self.radioButton_option2.setText('Apples')
            self.label_price2.show()
            self.label_price2.setText('$0.64/ea')
            self.frame_option3.show()
            self.radioButton_option3.setText('Carrots')
            self.label_price3.show()
            self.label_price3.setText('$1.34/lb')
            self.frame_option4.show()
            self.radioButton_option4.setText('Asparagus')
            self.label_price4.show()
            self.label_price4.setText('$3.57/ea')
        elif self.dropdown_list.currentIndex() == 1:
            self.frame_option1.show()
            self.radioButton_option1.setText('Blueberries')
            self.label_price1.show()
            self.label_price1.setText('$4.68/ea')
            self.frame_option2.show()
            self.radioButton_option2.setText('Mango')
            self.label_price2.show()
            self.label_price2.setText('$8.47/ea')
            self.frame_option3.show()
            self.radioButton_option3.setText('Bananas')
            self.label_price3.show()
            self.label_price3.setText('$2.47/ea')
            self.frame_option4.show()
            self.radioButton_option4.setText('Cherries')
            self.label_price4.show()
            self.label_price4.setText('$3.32/ea')
        elif self.dropdown_list.currentIndex() == 2:
            self.frame_option1.show()
            self.radioButton_option1.setText('Whole Wheat')
            self.label_price1.show()
            self.label_price1.setText('$3.48/lb')
            self.frame_option2.show()
            self.radioButton_option2.setText('Baguette')
            self.label_price2.show()
            self.label_price2.setText('$3.98/lb')
            self.frame_option3.show()
            self.radioButton_option3.setText('Ciabatta')
            self.label_price3.show()
            self.label_price3.setText('$3.54/lb')
            self.frame_option4.show()
            self.radioButton_option4.setText('Rye')
            self.label_price4.show()
            self.label_price4.setText('$1.65/lb')
        elif self.dropdown_list.currentIndex() == 3:
            self.frame_option1.show()
            self.radioButton_option1.setText('Chicken Breasts')
            self.label_price1.show()
            self.label_price1.setText('$3.94/lb')
            self.frame_option2.show()
            self.radioButton_option2.setText('N.Y. Steak')
            self.label_price2.show()
            self.label_price2.setText('$12.97/lb')
            self.radioButton_option3.show()
            self.radioButton_option3.setText('Bison Ribeye Steak')
            self.label_price3.show()
            self.label_price3.setText('$37.50/lb')
            self.frame_option4.show()
            self.radioButton_option4.setText('Duck Breast')
            self.label_price1.show()
            self.label_price1.setText('$18.48/lb')
        elif self.dropdown_list.currentIndex() == 4:
            self.frame_option1.show()
            self.radioButton_option1.setText('Takis')
            self.label_price1.show()
            self.label_price1.setText('$5.34/ea')
            self.frame_option2.show()
            self.radioButton_option2.setText('Sun Chips')
            self.label_price2.show()
            self.label_price2.setText('$4.49/ea')
            self.radioButton_option3.show()
            self.radioButton_option3.setText('Hot Cheetos')
            self.label_price3.show()
            self.label_price3.setText('$5.45/ea')
            self.frame_option4.show()
            self.radioButton_option4.setText('Funyuns')
            self.label_price4.show()
            self.label_price4.setText('$5.49/ea')
        elif self.dropdown_list.currentIndex() == 5:
            self.frame_option1.show()
            self.radioButton_option1.setText('Skinny POP')
            self.label_price1.show()
            self.label_price1.setText('$3.19/ea')
            self.frame_option2.show()
            self.radioButton_option2.setText('Trail Mix')
            self.label_price2.show()
            self.label_price2.setText('$5.02/ea')
            self.frame_option3.show()
            self.radioButton_option3.show()
            self.radioButton_option3.setText('Pistachios')
            self.label_price3.show()
            self.label_price3.setText('$5.49/ea')
            self.frame_option4.show()
            self.radioButton_option4.setText('Goldfish')
            self.label_price1.show()
            self.label_price1.setText('$2.64/ea')

    def add_to_cart(self) -> None:
        """adds the selected grocery and quantity to cart"""
        if self.radioButton_option1.isChecked():
            selected_items.append((self.radioButton_option1.text(), self.get_prices(1)))
            self.add_to_dictionary(1)
        if self.radioButton_option2.isChecked():
            selected_items.append((self.radioButton_option2.text(), self.get_prices(2)))
            self.add_to_dictionary(2)
        if self.radioButton_option3.isChecked():
            selected_items.append((self.radioButton_option3.text(), self.get_prices(3)))
            self.add_to_dictionary(3)
        if self.radioButton_option4.isChecked():
            selected_items.append((self.radioButton_option4.text(), self.get_prices(4)))
            self.add_to_dictionary(4)
        self.revert_radio_dropdown()

        print(cart)

    def add_to_dictionary(self, frame: int) -> None:
        """adds the selected groceries and quantities to a dictionary to keep track of
        number of items and total price of items"""
        for item_name_text, price in selected_items:
            quantity = getattr(self, f"dropdown_quantity{frame}").currentIndex() + 1
            item_name_text = getattr(self, f"radioButton_option{frame}").text()
            price = float(price)
            cart[item_name_text] = {'quantity': quantity, 'price': price}

        self.total = sum(item['price'] for item in cart.values())
        self.label_pretax_total.setText(f"${self.total:.2f}")

    def revert_radio_dropdown(self) -> None:
        """deactivates all radiobuttons and dropdown menu to first index"""
        self.radioButton_option1.setChecked(False)
        self.dropdown_quantity1.setCurrentIndex(0)
        self.radioButton_option2.setChecked(False)
        self.dropdown_quantity2.setCurrentIndex(0)
        self.radioButton_option3.setChecked(False)
        self.dropdown_quantity3.setCurrentIndex(0)
        self.radioButton_option4.setChecked(False)
        self.dropdown_quantity4.setCurrentIndex(0)

    def get_prices(self, frame) -> float:
        """gets the total price of each selected item"""
        quantity = getattr(self, f"dropdown_quantity{frame}").currentIndex() + 1
        item_cost_text = getattr(self, f"label_price{frame}").text()
        item_cost_text = re.search(r'\$([\d.]+)', item_cost_text)
        item_cost = item_cost_text.group(1)
        item_cost = float(item_cost)
        item_total = quantity * item_cost
        return item_total

    def checkout(self) -> None:
        """closes the MainWindow and opens the dialogue/checkout window"""
        for key in cart:
            print(key)
        self.close()
        checkout_window = Logic2(self)
        checkout_window.exec()


class Logic2(QDialog, Ui_SecondWindow):
    def __init__(self, parent=None) -> None:
        """set up for the checkout GUI"""
        super().__init__(parent)
        self.setupUi(self)
        self.label_receipt_items.hide()
        self.label_item_prices.hide()
        self.label_pretax_total.hide()
        self.label_tax.hide()
        self.label_total.hide()
        self.frame1.hide()
        self.label_thankyou_error.hide()
        self.button_return2shop.clicked.connect(lambda: self.return2shop())
        self.button_confirm_checkout.clicked.connect(lambda: self.confirm())
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_pay.clicked.connect(lambda: self.pay())

    def return2shop(self) -> None:
        """returns to MainWindow to continue shopping"""
        self.accept()

        if self.parent() is not None:
            self.parent().show()

    def confirm(self) -> None:
        """confirms that user wants to proceed to checkout"""
        self.cart_info = []
        cart_prices = []

        for item_name, item_info in cart.items():
            self.quantity = str(item_info['quantity'])
            self.price = f"${item_info['price']:.2f}"
            self.cart_info.append(f"{item_name} x {self.quantity}")
            cart_prices.append(self.price)

        cart_prices = [s.replace('$', "") for s in cart_prices]
        cart_prices = [float(position) for position in cart_prices]
        self.cart_total = sum(cart_prices)

        self.label_receipt_items.show()
        self.label_receipt_items.setText('\n'.join(self.cart_info))

        cart_prices = [str(position) for position in cart_prices]
        self.label_item_prices.show()
        self.label_item_prices.setText('\n'.join(cart_prices))

        self.label_pretax_total.show()
        self.label_pretax_total.setText(f"Subtotal: ${self.cart_total:.2f}")

        self.label_tax.show()
        self.tax_amount = self.cart_total * 0.07
        self.label_tax.setText(f"Tax (7%): ${self.tax_amount:.2f}")

        self.label_total.show()
        self.total = self.cart_total + self.tax_amount
        self.label_total.setText(f"Total: ${self.total:.2f}")

        self.frame1.show()

        self.label_cash_card.hide()
        self.input_cash_card.hide()
        self.button_pay.hide()
        self.label_thankyou_error.hide()

    def submit(self) -> None:
        """opens the payment method to cash or card depending on which radioButton is selected"""
        if self.radioButton_cash.isChecked():
            self.label_cash_card.show()
            self.label_cash_card.setText('Enter Cash Amount')
            self.input_cash_card.show()
            self.button_pay.show()
        elif self.radioButton_card.isChecked():
            self.label_cash_card.show()
            self.label_cash_card.setText('Enter 16-digit Card Number')
            self.input_cash_card.show()
            self.button_pay.show()
        else:
            self.label_cash_card.setText('Please Choose a Payment Method')

    def pay(self) -> None:
        """processes the payment type and checks for valid payment quantity and methods"""
        if self.radioButton_cash.isChecked():
            user_paid_amount = self.input_cash_card.text()
            try:
                user_paid_amount = float(user_paid_amount)
                if user_paid_amount >= self.total:
                    self.label_thankyou_error.show()
                    user_change = user_paid_amount - self.total
                    self.clear()
                    self.label_thankyou_error.setText(f"Thank you for Shopping at V.S Grocery. \n"
                                                    f"Your change is: ${user_change:.2f}")
                else:
                    self.label_thankyou_error.show()
                    self.label_thankyou_error.setText('Insufficient to Pay. Pay again')
            except ValueError:
                self.label_thankyou_error.show()
                self.label_thankyou_error.setText('Enter a Valid Cash Amount')
        elif self.radioButton_card.isChecked():
            user_card_num = self.input_cash_card.text()
            user_card_num = user_card_num.strip()
            try:
                if len(user_card_num) == 16 and user_card_num.isdigit():
                    user_card_num = int(user_card_num)
                    self.clear()
                    self.label_thankyou_error.show()
                    self.label_thankyou_error.setText('Approved. Thank you for Shopping at V.S. Grocery')
                else:
                    self.label_thankyou_error.show()
                    self.label_thankyou_error.setText('Invalid Enter a Valid Credit Card Number')
            except ValueError:
                self.label_thankyou_error.show()
                self.label_thankyou_error.setText('Enter a Valid Credit Card Number')
        self.input_cash_card.clear()

    def clear(self) -> None:
        """clears the Checkout window to "exit" the store"""
        self.label_checkout.hide()
        self.button_return2shop.hide()
        self.button_confirm_checkout.hide()
        self.label_receipt_items.hide()
        self.label_item_prices.hide()
        self.label_pretax_total.hide()
        self.label_tax.hide()
        self.label_total.hide()
        self.frame1.hide()
