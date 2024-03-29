import turtle as tu

class GOJO:
    def __init__(self,x_offset = 300, y_offset = 300):
        '''x_offset and y_offset represents the position of the image being drawn, by default it is 300 you can change it any coordinates you want'''
        import turtle as tu
        self.tu = tu
        self.mask = [(137, 213),(146, 213),(160, 216),(187, 219),(219, 222),(267, 225),(292, 225),(332, 225),(366, 225),(401, 225),(424, 216),(430, 214),(428, 225),(424, 244),(412, 261),(420, 252),(421, 266),(404, 284),(420, 271),(418, 277),(413, 285),(404, 295),(389, 308),(369, 321),(333, 333),(314, 323),(305, 316),(292, 311),(257, 333),(246, 333),(166, 297),(147, 274),(148, 255),(170, 272),(146, 253),(144, 236),(142, 226),(137, 212),]
        self.hair = [(135, 213),(111, 213),(94, 217),(83, 224),(93, 216),(122, 204),(110, 200),(91, 199),(79, 197),(60, 202),(60, 200),(73, 192),(101, 180),(89, 172),(75, 162),(52, 142),(59, 143),(88, 151),(108, 153),(85, 153),(60, 124),(70, 131),(98, 147),(108, 150),(97, 144),(80, 127),(55, 96),(67, 101),(74, 104),(102, 109),(117, 109),(126, 104),(118, 107),(99, 108),(85, 97),(76, 83),(90, 92),(104, 98),(119, 100),(108, 97),(92, 91),(153, 79),(156, 74),(153, 79),(139, 81),(113, 61),(99, 45),(96, 39),(114, 54),(129, 60),(145, 65),(129, 47),(121, 34),(114, 17),(109, 2),(117, 8),(132, 20),(152, 29),(162, 33),(179, 35),(186, 36),(174, 28),(163, 20),(158, 10),(154, 3),(162, 4),(168, 9),(183, 16),(196, 22),(209, 25),(222, 28),(229, 28),(224, 18),(217, 12),(211, 4),(218, 4),(223, 10),(233, 14),(242, 20),(249, 31),(251, 33),(242, 22),(239, 13),(236, 4),(234, 1),(246, 3),(261, 12),(269, 21),(274, 28),(260, 12),(254, 0),(262, 3),(288, 11),(304, 17),(320, 24),(329, 33),(311, 15),(304, 2),(314, 2),(328, 9),(335, 21),(348, 29),(355, 40),(369, 52),(363, 28),(357, 1),(380, 21),(391, 42),(402, 69),(404, 87),(401, 71),(418, 10),(417, 1),(423, 18),(435, 61),(438, 82),(435, 107),(429, 124),(433, 108),(454, 84),(464, 59),(465, 69),(461, 90),(457, 107),(449, 126),(439, 143),(435, 148),(460, 132),(487, 116),(493, 109),(484, 128),(474, 141),(469, 147),(450, 162),(476, 136),(458, 163),(448, 173),(492, 146),(489, 156),(476, 167),(457, 183),(474, 191),(497, 210),(488, 205),(475, 204),(441, 204),(441, 207),(464, 214),(483, 228),(458, 219),(431, 215),(422, 215),(324, 225),(273, 226),(193, 220),(138, 212),]
        self.dress = [(198, 400),(199, 432),(214, 433),(210, 423),(214, 432),(235, 434),(295, 444),(301, 440),(379, 453),(388, 458),(430, 464),(499, 447),(442, 423),(381, 415),(375, 453),(302, 439),(298, 444),(289, 561),(113, 539),(94, 443),(86, 428),(90, 421),(101, 427),(112, 435),(181, 441),(243, 451),(273, 457),(288, 460),(296, 471),(296, 479),(293, 525),(270, 525),(244, 532),(204, 518),(188, 511),(155, 512),(157, 515),(191, 530),(229, 537),(278, 550),(292, 556),(291, 560),(292, 555),(350, 556),(371, 498),(306, 475),(299, 488),(290, 561),(373, 559),(387, 471),(381, 504),(395, 491),(448, 503),(460, 497),(445, 528),(415, 554),(372, 560),(461, 560),(478, 537),(476, 514),(463, 527),(477, 510),(504, 449),(380, 413),(378, 454),(305, 439),(296, 444),(198, 433),(198, 400),(136, 416),(109, 421),(86, 420),(87, 426),(95, 424),]
        self.face = [(145, 275),(143, 273),(136, 279),(135, 308),(139, 323),(146, 333),(154, 342),(170, 360),(181, 363),(170, 311),(164, 311),(146, 285),(140, 283),(143, 284),(142, 301),(150, 294),(157, 304),(153, 305),(153, 323),(154, 331),(175, 350),(175, 339),(168, 334),(170, 320),(165, 321),(170, 319),(186, 384),(194, 395),(234, 435),(298, 444),(305, 438),(339, 446),(396, 365),(408, 304),(410, 304),(412, 313),(410, 305),(429, 277),(427, 295),(420, 289),(413, 299),(418, 299),(419, 315),(407, 338),(398, 340),(397, 357),(406, 355),(413, 340),(432, 316),(434, 274),(429, 267),(417, 274),(414, 284),(410, 291),]
        self.face_shades = [(196, 220),(295, 232),(304, 242),(295, 262),(294, 284),(296, 284),(336, 238),(407, 231),(406, 248),(390, 264),(411, 257),(391, 281),(406, 274),(403, 279),(379, 304),(390, 300),(380, 311),(332, 336),(302, 315),(297, 295),(295, 290),(291, 294),(291, 309),(255, 331),(249, 314),(279, 296),(265, 301),(275, 285),(278, 277),(275, 265),(260, 252),(267, 257),(265, 258),(253, 259),(227, 250),(231, 247),(242, 249),(222, 241),(196, 233),(189, 230),(194, 219),(291, 225),(424, 215),(436, 212),(356, 222),(293, 226),(195, 222),(146, 212),(142, 214),(151, 247),(171, 270),(171, 272),(159, 263),(158, 277),(169, 287),(162, 282),(161, 290),(253, 334),(294, 310),(291, 351),(295, 368),(306, 367),(298, 367),(304, 369),(297, 369),(306, 371),(294, 387),(275, 368),(281, 368),(288, 369),(281, 369),(288, 369),(277, 370),(262, 358),(258, 343),(247, 345),(232, 378),(261, 439),]
        self.mouth = [(322, 262),(336, 249),(348, 248),(393, 253),(384, 256),(347, 257),(328, 266),(320, 265),(325, 268),(336, 261),(339, 265),(322, 274),(326, 276),(342, 271),(373, 268),(373, 264),(342, 264),(327, 272),(322, 282),(313, 291),(331, 316),(367, 303),(346, 304),(339, 302),(329, 294),(322, 288),(322, 282),(323, 292),(345, 304),(370, 304),(379, 303),(387, 301),(382, 310),(331, 336),(307, 315),(290, 311),(295, 368),(300, 368),(306, 368),(299, 368),(306, 368),(293, 385),(295, 400),(280, 400),(317, 400),(316, 400),(278, 402),(318, 402),(279, 401),(319, 402),(326, 399),(336, 398),(328, 401),(335, 398),(326, 399),(338, 399),(291, 401),(278, 399),(263, 398),(253, 397),(265, 400),(255, 396),(267, 399),(258, 397),(268, 400),(254, 397),(268, 401),(296, 399),(296, 411),(281, 411),(310, 410),(285, 409),(306, 408),(307, 411),(282, 410),(310, 408),(284, 410),(307, 410),(284, 410),(308, 410),]
        self.dress_extra = [(385, 385),(379, 454),(307, 439),(298, 446),(245, 437),(198, 434),(128, 428),(116, 428),(99, 424),(89, 420),(89, 426),(91, 421),(101, 424),(148, 414),(198, 405),(198, 397),(188, 391),(180, 359),(172, 362),(139, 323),(136, 278),(143, 275),(169, 299),(254, 332),(248, 314),(247, 301),(237, 302),(243, 297),(254, 288),(260, 287),(258, 293),(246, 302),(257, 292),(258, 288),(258, 273),(244, 260),(214, 260),(214, 262),(237, 264),(240, 269),(253, 276),(260, 272),(246, 261),(246, 258),(225, 247),(242, 247),(257, 252),(266, 259),(261, 259),(246, 259),]
        self.hair_shade = [(196, 222),(189, 209),(164, 196),(179, 204),(195, 221),(209, 223),(197, 198),(155, 174),(180, 186),(206, 219),(275, 227),(254, 191),(212, 163),(262, 200),(272, 223),(278, 213),(259, 166),(281, 210),(286, 223),(323, 222),(328, 215),(313, 162),(305, 206),(307, 181),(270, 95),(290, 116),(263, 49),(316, 95),(300, 61),(283, 38),(312, 60),(326, 75),(313, 41),(290, 10),(318, 24),(332, 31),(308, 3),(359, 38),(377, 66),(356, 1),(407, 90),(403, 69),(417, 2),(437, 58),(430, 125),(416, 149),(398, 167),(377, 202),(372, 200),(361, 219),(375, 192),(384, 153),(371, 195),(360, 219),(341, 224),(357, 157),(349, 195),(339, 220),(352, 184),(358, 150),(350, 99),(360, 128),(359, 147),(372, 151),(370, 96),(351, 48),(369, 95),(372, 148),(381, 152),(374, 126),(378, 147),(387, 138),(379, 149),]
        self.r_glass = [(272, 249),(262, 252),(258, 259),(256, 264),(254, 272),(254, 280),(256, 289),(260, 298),(263, 301),(271, 307),(276, 309),(283, 311),(289, 312),(296, 313),(301, 311),(308, 306),(313, 299),(319, 289),(321, 282),(323, 274),(322, 270),(319, 266),(310, 260),(299, 255),(292, 252),(278, 249),(273, 249),(267, 250),(263, 251),(260, 254)]
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = x_offset
        self.y_offset = y_offset


    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        self.pen.pendown()  


    def paint(self,coord,co=(0,0,0)):
        self.pen.color(co)
        t_x,t_y = coord[0]
        self.go(t_x,t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            #print(i)
            x,y = i
            if t:
                self.go(x,y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset) 
        self.pen.end_fill()


    def draw_fn(self,coord,mode = 1,co = (0,0,0),thickness = 1):
        co = (co[0]/255,co[1]/255,co[2]/255)

        self.pen.color(co)

        if mode:
            self.pen.width(thickness)
            t_x,t_y = coord[0]
            self.go(t_x,t_y)
            t = 0
            for i in coord[1:]:
                #print(i)
                x,y = i
                if t:
                    self.go(x,y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        else:
            self.paint(coord=coord,co = co)

    
    def draw(self,retain=True):
        self.draw_fn(self.mask)
        self.draw_fn(self.hair)
        self.draw_fn(self.face)
        self.draw_fn(self.dress)
        self.draw_fn(self.face_shades)
        self.draw_fn(self.mouth)
        self.draw_fn(self.dress_extra)
        self.draw_fn(self.hair_shade)
        if retain:
            self.tu.done()
            

if __name__ == "__main__":
    tu.setup(1000, 1000)
    gojo = GOJO()
    gojo.draw()
