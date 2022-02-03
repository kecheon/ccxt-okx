# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.coinbasepro import coinbasepro


class coinbaseprime(coinbasepro):

    def describe(self):
        return self.deep_extend(super(coinbaseprime, self).describe(), {
            'id': 'coinbaseprime',
            'name': 'Coinbase Prime',
            'pro': True,
            'hostname': 'exchange.coinbase.com',
            'urls': {
                'test': {
                    'public': 'https://public.sandbox.exchange.coinbase.com',
                    'private': 'https://public.sandbox.exchange.coinbase.com',
                },
                'logo': 'https://user-images.githubusercontent.com/1294454/44539184-29f26e00-a70c-11e8-868f-e907fc236a7c.jpg',
                'api': {
                    'public': 'https://api.{hostname}',
                    'private': 'https://api.{hostname}',
                },
                'www': 'https://exchange.coinbase.com',
                'doc': 'https://docs.exchange.coinbase.com',
            },
        })
