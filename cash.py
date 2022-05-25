from decimal import Decimal, InvalidOperation


class CoinChangeCalculator:
    def __init__(self):
        self.coins = [
            '0.25',  # quarters
            '0.10',  # dimes
            '0.05',  # nickels
            '0.01'   # pennies
        ]
        # using Decimal instead of float to avoid impressions problems
        self.coins = [Decimal(x) for x in self.coins]
        # Coins are sorted by its value to use first the greater value
        self.coins.sort(reverse=True)

    def get_minimum_coins_number_brute(self, amount: 'Decimal'):
        """
            Gets the minimum coins using brute force
        :param amount:
        :return:
        """
        current_coin_index = 0
        coin_count = 0
        while amount > 0 and current_coin_index < len(self.coins):
            if amount >= self.coins[current_coin_index]:
                coin_count += 1
                amount -= self.coins[current_coin_index]
            else:
                current_coin_index += 1
        return coin_count

    def get_minimum_coins_number(self, amount: 'Decimal'):
        """
            Gets the minimum coins using simplified method
            Warning, if the amount is lower than the minimum coin it dont be considered
            Ex:
                amount = 0.001
                output : 0

        :param amount:
        :return:
        """
        current_coin_index = 0
        coin_count = 0
        while amount > 0 and current_coin_index < len(self.coins):
            if amount >= self.coins[current_coin_index]:
                number_coins = amount // self.coins[current_coin_index]
                coin_count += number_coins
                amount -= self.coins[current_coin_index] * number_coins
            current_coin_index += 1
        return coin_count


class MainMenu:
    def run(self):
        while True:
            val = input("Change owed: ")
            try:
                val = Decimal(val)
                assert val > 0
                return val
            except InvalidOperation:
                pass
            except AssertionError:
                pass


if __name__ == '__main__':
    menu = MainMenu()
    change_owed = menu.run()
    coins = CoinChangeCalculator().get_minimum_coins_number(change_owed)
    print(coins)
