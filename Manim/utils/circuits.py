from manim import *


class RLC_circuit(Scene):
        
    def create_simple_RLC(self, factor_L1=0.4, factor_R1=0.4):
        
        #-----------------------------------------------------------------------
        ## Upper dot and line

        klemme_l_o = Circle(radius = 0.1,color=WHITE)
        klemme_l_o.shift(LEFT*5+UP*2)

        line_klemme_l_o_Rs = Line(LEFT,RIGHT*(1-factor_L1))
        line_klemme_l_o_Rs.next_to(klemme_l_o.get_corner(RIGHT), RIGHT,buff=0)

        #-----------------------------------------------------------------------
        ## Resistor: Rs
        Rs = Rectangle(height=0.5, width=1+2*factor_L1)
        Rs.next_to(line_klemme_l_o_Rs.get_corner(RIGHT), RIGHT,buff=0)
        Rs_text = Tex('$R$')
        Rs_text.next_to(Rs, UP)

        #-----------------------------------------------------------------------
        ## Line to inductor: L

        line_Rs_L = Line(LEFT,RIGHT*(1-factor_L1))
        line_Rs_L.next_to(Rs.get_corner(RIGHT), RIGHT,buff=0)

        L1 = Rectangle(height=0.5, width=1+2*factor_L1)
        L1.set_fill(WHITE,opacity=1)
        L1.next_to(line_Rs_L.get_corner(RIGHT), RIGHT,buff=0)
        L1_text = Tex('$L$')
        L1_text.next_to(L1, UP)

        #-----------------------------------------------------------------------
        ## Corner to capacity: C

        line_L1_corner = Line(LEFT,RIGHT*(1-factor_L1))
        line_L1_corner.next_to(L1.get_corner(RIGHT), RIGHT,buff=0)

        line_corner_C1 = Line(UP,DOWN*(1-factor_L1))
        line_corner_C1.next_to(line_L1_corner.get_corner(RIGHT), DOWN, buff=0)

        #-----------------------------------------------------------------------
        ## Capacity: C

        line_C1_plus = Line(LEFT,RIGHT)
        line_C1_plus.next_to(line_corner_C1.get_corner(DOWN),DOWN,buff=0)

        line_C1_minus = Line(LEFT,RIGHT)
        line_C1_minus.next_to(line_corner_C1.get_corner(DOWN),UP,buff=-0.4)

        C1_text = Tex('$C$')
        C1_text.next_to(line_C1_plus.get_corner(RIGHT)+DOWN*0.25, RIGHT)

        #-----------------------------------------------------------------------
        ## Corner back 

        line_C1_down = Line(UP,DOWN*(1-factor_L1))
        line_C1_down.next_to(line_C1_minus.get_center(), DOWN,buff=0)

        line_corner_back = Line(line_klemme_l_o_Rs.get_corner(LEFT), 
                                line_L1_corner.get_corner(RIGHT))
        line_corner_back.next_to(line_C1_down.get_corner(DOWN), LEFT, buff=0)

        #-----------------------------------------------------------------------
        ## Lower dot

        klemme_r_u = Circle(radius = 0.1,color=WHITE)
        klemme_r_u.next_to(line_corner_back.get_corner(LEFT), LEFT, buff=0)

        #-----------------------------------------------------------------------
        ## u(t)

        U_e = CurvedArrow(line_klemme_l_o_Rs.get_corner(LEFT),
                          line_corner_back.get_corner(LEFT),
                          angle=TAU/4, color=BLUE)
        U_e.next_to(klemme_l_o.get_corner(LEFT) + 0.1*LEFT,
                    klemme_r_u.get_corner(LEFT) + 0.1*LEFT,
                    buff=0.0)

        UE_text = Tex('$u(t)=\sqrt{2} U_{eff} \sin{(\omega t + \phi)}$',color=BLUE)
        UE_text.next_to(U_e.get_center(), RIGHT*0.1)

        #-----------------------------------------------------------------------
        ## i(t)

        current = Triangle().scale(0.2).rotate(-90*DEGREES)
        current.set_fill(RED,opacity=1).set_color(RED)
        current.next_to(line_klemme_l_o_Rs.get_center(), RIGHT*0)

        current_text = Tex('$i(t)$',color=RED)
        current_text.next_to(current.get_center(), UP)
        
        list_objects =   [klemme_l_o, line_klemme_l_o_Rs, Rs, Rs_text,
                          line_Rs_L, L1, L1_text, line_L1_corner, 
                          line_corner_C1, line_C1_plus, line_C1_minus, 
                          C1_text, line_C1_down, line_corner_back, klemme_r_u]

        self.circuit = VGroup(*list_objects)
        self.vol_curr = VGroup(U_e, UE_text, current, current_text)
        
        return self.circuit, self.vol_curr
    
    def create_extended_RLC(self,factor_L1=0.4, factor_R1=0.4):
        
        circuit, vol_curr = self.create_simple_RLC()
        
        knoten1 = Circle(radius = 0.1,color=WHITE, fill_color=WHITE).set_fill(WHITE,opacity=1)
        knoten1.next_to(circuit[7].get_corner(RIGHT), RIGHT*0, buff=0)
        knoten2 = Circle(radius = 0.1,color=WHITE, fill_color=WHITE).set_fill(WHITE,opacity=1)
        knoten2.next_to(circuit[13].get_corner(RIGHT), RIGHT*0, buff=0)
        
        line_corner_UP = Line(LEFT,RIGHT*2)
        line_corner_UP.next_to(circuit[7].get_corner(RIGHT), RIGHT,buff=0)
        line_corner_BOTTOM = Line(LEFT,RIGHT*2)
        line_corner_BOTTOM.next_to(circuit[13].get_corner(RIGHT), RIGHT,buff=0)
        
        line_corner_vert_1 = Line(UP,-DOWN*0.1)
        line_corner_vert_1.next_to(line_corner_UP.get_corner(RIGHT), DOWN, buff=0)
        line_corner_vert_2 = Line(UP,-DOWN*0.1)
        line_corner_vert_2.next_to(line_corner_BOTTOM.get_corner(RIGHT), UP, buff=0)
        
        
        Rp = Rectangle(height=1+2*factor_L1, width=0.5)
        Rp.next_to(line_corner_vert_1.get_corner(DOWN), DOWN,buff=0)
        Rp_text = Tex('$R_p$')
        Rp_text.next_to(Rp, RIGHT)
        
        circuit.add(knoten1,knoten2,line_corner_UP,line_corner_BOTTOM,line_corner_vert_1,line_corner_vert_2, Rp, Rp_text)
        return circuit, vol_curr
        
        
class RLC_elements(Scene):
        
    def create_R(self, factor_line=0.4, factor_R1=0.8):
        
        knoten1 = Circle(radius = 0.1, color=WHITE)
        
        line_corner_UP = Line(LEFT,RIGHT*0)
        line_corner_UP.next_to(knoten1.get_corner(RIGHT), RIGHT,buff=0)
        
        line_corner_vert_1 = Line(UP,DOWN*factor_line)
        line_corner_vert_1.next_to(line_corner_UP.get_corner(RIGHT), DOWN, buff=0)
        
        Rp = Rectangle(height=1+factor_R1, width=0.5)
        Rp.next_to(line_corner_vert_1.get_corner(DOWN), DOWN,buff=0)
        Rp_text = Tex('$R$')
        Rp_text.next_to(Rp, RIGHT)
        
        line_corner_vert_2 = Line(UP,DOWN*factor_line)
        line_corner_vert_2.next_to(Rp.get_corner(DOWN), DOWN, buff=0)
        
        line_corner_BOTTOM = Line(LEFT*0,RIGHT)
        line_corner_BOTTOM.next_to(line_corner_vert_2.get_corner(DOWN), LEFT, buff=0)
        
        knoten2 = Circle(radius = 0.1, color=WHITE)
        knoten2.next_to(line_corner_BOTTOM.get_corner(LEFT), LEFT, buff=0)
        

        element = VGroup(knoten1, line_corner_UP, line_corner_vert_1, 
                         Rp, Rp_text, line_corner_vert_2, line_corner_BOTTOM, knoten2)
        
        return element
    
    def create_L(self):
        element = self.create_R()
        element[3].set_fill(WHITE,opacity=1)
        element[4] = Tex('$L$').next_to(element[3], RIGHT)
        return element
        
        
    def create_C(self, factor_line=0.4, factor_C=0.3):
        
        knoten1 = Circle(radius = 0.1, color=WHITE)
        
        line_corner_UP = Line(LEFT,RIGHT*0)
        line_corner_UP.next_to(knoten1.get_corner(RIGHT), RIGHT,buff=0)
        
        line_corner_vert_1 = Line(UP,DOWN*factor_line)
        line_corner_vert_1.next_to(line_corner_UP.get_corner(RIGHT), DOWN, buff=0)
        
        line_C1_plus = Line(LEFT,RIGHT*factor_C)
        line_C1_plus.next_to(line_corner_vert_1.get_corner(DOWN),DOWN,buff=0)

        line_C1_minus = Line(LEFT,RIGHT*factor_C)
        line_C1_minus.next_to(line_corner_vert_1.get_corner(DOWN),UP,buff=-0.4)

        C1_text = Tex('$C$')
        C1_text.next_to(line_C1_plus.get_corner(RIGHT)+DOWN*0.25, RIGHT)
        
        line_corner_vert_2 = Line(UP,DOWN*factor_line)
        line_corner_vert_2.next_to(line_C1_minus.get_center(), DOWN, buff=0)
        
        line_corner_BOTTOM = Line(LEFT*0,RIGHT)
        line_corner_BOTTOM.next_to(line_corner_vert_2.get_corner(DOWN), LEFT, buff=0)
        
        knoten2 = Circle(radius = 0.1, color=WHITE)
        knoten2.next_to(line_corner_BOTTOM.get_corner(LEFT), LEFT, buff=0)
        

        element = VGroup(knoten1, line_corner_UP, line_corner_vert_1, line_C1_plus,  
                        line_C1_minus, C1_text, line_corner_vert_2, line_corner_BOTTOM, knoten2)
        
        return element