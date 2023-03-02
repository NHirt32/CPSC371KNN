
# Switches an alphabetical character to a number representation
# 1) To utilize you must import input_switcher.py
# 2) Create an instance object "switcher = input_switcher.input_switcher()"
# 3) Then you can use the switch method to switch the input
#       attr = switcher.switch('a')
class input_switcher:

    def switch(self, attribute):
        default = '?'
        return getattr(self, 'case_' + str(attribute), lambda: default)()

    def case_a(self):
        return 0

    def case_b(self):
        return 1

    def case_c(self):
        return 2

    def case_d(self):
        return 3

    def case_e(self):
        return 4

    def case_f(self):
        return 5

    def case_g(self):
        return 6

    def case_h(self):
        return 7

    def case_i(self):
        return 8

    def case_j(self):
        return 9

    def case_k(self):
        return 10

    def case_l(self):
        return 11

    def case_m(self):
        return 12

    def case_n(self):
        return 13

    def case_o(self):
        return 14

    def case_p(self):
        return 15

    def case_q(self):
        return 16

    def case_r(self):
        return 17

    def case_s(self):
        return 18

    def case_t(self):
        return 19

    def case_u(self):
        return 20

    def case_v(self):
        return 21

    def case_w(self):
        return 22

    def case_x(self):
        return 23

    def case_y(self):
        return 24

    def case_z(self):
        return 25
