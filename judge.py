import copy

class judge:
    def __init__(self):
        self.card_dic = {}
        self.init_card_list()
        # initialize card list 
        self.my_card = []
        self.dealer_card =6
        self.total_num = 0
        self.judgement_in_betting = False
        self.burst_num=21
        # If judgemnet in betting is False 
        #     False => no betting
        # not False => betting Rate
        # Total num is Sum of Card What i have
    def init_card_list(self):
        for i in range(1,10):
            self.card_dic[i] = 4
        self.card_dic[10] = 16
        # Card have four picture 
        # In this Case, Picture of Card do not influence Game
        # What we need is only number of card remains

    def judge(self):
        self.dealer_probabilty={}
        self.total_card = 0
        for i in range(22):
            self.dealer_probabilty[i]=0
            if i in self.card_dic.keys():
                self.total_card += self.card_dic[i]
        # initalize dealer_case

        self.tmp_card_dic=copy.copy(self.card_dic)
        print(self.tmp_card_dic)
        self.dealer_case_find(1,self.tmp_card_dic,self.dealer_card,self.total_card,False)
        # initial my card total num


        #######  Debugging Logic ##########
        sum=0
        for i in self.dealer_probabilty.keys():
            sum += self.dealer_probabilty[i]
        for i in self.dealer_probabilty.keys():
            print("{} : {}".format(i,self.dealer_probabilty[i]/sum))

        ###### Debugging Logic #############

        ##Check Win Rate
        self.hit_rate={}
        
    def stay_win_rate(self):
        rate=0
        for dealer_total in self.dealer_probabilty():
            if dealer_total == 0:
                # Dealer Bust
                rate +=self.dealer_probabilty[dealer_total]
            elif self.total_num > dealer_total:
                rate +=self.dealer_probabilty[dealer_total]


    def dealer_case_find(self,prob,card_dic,total,card_num,ace_check):
        if total > self.burst_num:
            # Burst
            if ace_check == True:
                total -=10
                ace_check = False

                tmp_dic=copy.copy(card_dic)
                self.dealer_case_find(prob,tmp_dic,total,card_num,ace_check)
            else:
                self.dealer_probabilty[0] += prob
        elif total >16:
            self.dealer_probabilty[total] += prob
        
        else:
            card_num -= 1
            # Draw one Card More
            for i in card_dic.keys():
                tmp_dic=copy.copy(card_dic)
                tmp_ace_check=ace_check
                tmp_total=total
                tmp_prob = prob
                tmp_card_num = card_num
                if tmp_dic[i]>0:
                    if i ==1:
                        tmp_ace_check = True
                        tmp_total += 10
                        
                    tmp_prob *= (tmp_dic[i]/tmp_card_num)
                    tmp_dic[i] -= 1
                    tmp_total += i
                    self.dealer_case_find(tmp_prob,tmp_dic,tmp_total,tmp_card_num,tmp_ace_check)

                    

    def input(self,my_card_first,my_card_second,dealer_card):
        self.my_card.append(my_card_first)
        self.my_card.append(my_card_second)
        self.total_num= my_card_first+ my_card_second
        # total_num _ plus
        for card in self.my_card:
            self.card_dic[card] -=1
        # pop my card in my card dic

        self.dealer_card = dealer_card
        # Input is only open Card
        self.card_dic[dealer_card] -=1
        # pop dealer card in my card dic


    def output(self):

        return self.judgement_in_betting
        # Return Betting Rate

    def end_game(self,dealer_card_hid):


        for card in dealer_card_hid:
            self.card_dic[card] -=1
        # pop hidden dealer card in my card dic

        self.my_card=[]
        self.judgement_in_betting = False
        self.total_num=0
        # Reinitialize mycard list for next use



        # 할 수 있는 결과
        # Hit => 카드 한장 더 받기
        # Double => 카드를 한장만 더 받는 조건으로 배팅 2배
        # Stay => 멈추기

        # Stay => 종료
        # Double => 카드를 한장 더 받고 종료
        # Hit => 카드를 Stay 할 때 까지 받음

        # 처음 입력(self.input() )을 통해 카드 두장과 딜러카드 한장을 입력을 받고
        # 판단 => Hit , Double, Stay => self.output()
        # Double => 카드 하나 더 입력 => End
        # Stay => 종료 => 딜러 카드 확인 => End
        # Hit => 카드 하나 더 입력, Stay,Hit 판단
        # Double 처음 판단이 Double이 아니라면 Stay까지 카드를 받음
        
        # input 
        # 카드를 빼준다(카드를 이미 봤으니 숨겨진 카드에는 없다고 생각)
        #

        ## judge
        # 처음 카드를 받고
        # 내가 Burst 나도 0, 딜러한테 져도 0 