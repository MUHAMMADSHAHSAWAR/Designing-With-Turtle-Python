import turtle as tu


class VIJAY:
    def __init__(self, x_offset=270, y_offset=300):
        '''x_offset and y_offset represents the position of the image being drawn, by default it is 300 you can change it any coordinates you want'''
        import turtle as tu
        self.dress = [(149, 348), (152, 344), (151, 333), (144, 335), (137, 337), (103, 372), (101, 378), (67, 389), (59, 389), (53, 391), (8, 404), (17, 440), (37, 487), (65, 523), (80, 544), (98, 570), (124, 601), (164, 620), (201, 646), (222, 660), (236, 665), (262, 663), (301, 658), (336, 649), (364, 639), (399, 612), (415, 591), (420, 585), (414, 562), (405, 542), (389, 523), (375, 508), (378, 501), (378, 494), (380, 483),
                      (370, 470), (336, 440), (300, 408), (281, 443), (292, 459), (296, 470), (299, 474), (297, 493), (300, 513), (286, 527), (276, 542), (262, 587), (244, 640), (231, 598), (204, 557), (191, 524), (186, 520), (186, 514), (185, 508), (180, 501), (177, 484), (168, 478), (160, 467), (156, 430), (153, 409), (147, 394), (142, 376), (142, 372), (142, 366), (145, 358), (148, 352), (150, 349), (151, 343), (149, 335), (146, 335)]
        self.glass_frame = [(156, 223), (158, 214), (202, 220), (282, 244), (337, 270), (345, 275), (358, 284), (357, 292), (337, 278), (331, 278), (329, 279), (324, 290), (318, 300), (312, 307), (307, 311), (302, 314), (297, 315), (291, 315), (286, 315), (280, 314), (272, 311), (
            264, 306), (258, 300), (254, 293), (250, 281), (251, 264), (253, 251), (244, 247), (235, 245), (230, 259), (224, 271), (209, 284), (202, 285), (192, 285), (181, 283), (172, 279), (164, 272), (160, 262), (159, 251), (159, 238), (160, 226), (156, 222), (158, 215)]
        self.hair = [(156, 220), (159, 214), (178, 215), (205, 163), (209, 157), (211, 155), (217, 155), (229, 157), (256, 164), (251, 165), (259, 171), (253, 170), (259, 175), (253, 175), (256, 177), (251, 179), (257, 182), (271, 182), (265, 180), (275, 180), (267, 175), (278, 179), (272, 173), (301, 180), (313, 187), (310, 178), (316, 181), (324, 186), (325, 183), (334, 190), (347, 198), (353, 203), (353, 210), (350, 216), (346, 227), (341, 238), (340, 243), (337, 255), (339, 266), (341, 254), (342, 266), (343, 261), (348, 259), (350, 260), (350, 270), (348, 278), (351, 275), (351, 279), (353, 278), (354, 280), (354, 282), (356, 279), (357, 284), (358, 281), (358, 285), (357, 286), (356, 295), (355, 291), (354, 293), (353, 299), (351, 296), (350, 300), (350, 309), (348, 305), (348, 312), (347, 314), (346, 318), (345, 315), (344, 321), (343, 330), (341, 337), (333, 346), (327, 359), (327, 354), (325, 359), (324, 356), (319, 361), (321, 355), (316, 361), (316, 356), (313, 361), (314, 353), (307, 361), (311, 353), (305, 359), (306, 353), (290, 370), (294, 364), (278, 380), (275, 382), (268, 384), (266, 380), (266, 369), (269, 364), (273, 357), (274, 351), (272, 343), (267, 332), (266, 335), (262, 331), (262, 333), (258, 327), (258, 329), (255, 325), (255, 328), (251, 322), (250, 324), (246, 321), (246, 323), (241, 319), (238, 317), (232, 315), (228, 319), (222, 317), (220, 313), (217, 309), (210, 309), (203, 308), (203, 310), (194, 312), (187, 313), (181, 316), (177, 321), (174, 329), (172, 335), (172, 344), (175, 341), (
            167, 351), (162, 344), (162, 337), (160, 341), (160, 333), (158, 336), (157, 329), (155, 321), (153, 313), (150, 307), (150, 300), (150, 291), (146, 305), (146, 316), (145, 324), (146, 334), (146, 345), (153, 354), (158, 367), (163, 375), (168, 388), (170, 395), (174, 401), (176, 398), (178, 404), (178, 404), (181, 404), (187, 410), (195, 411), (204, 418), (211, 424), (214, 422), (221, 423), (225, 426), (230, 424), (233, 428), (237, 425), (245, 425), (250, 423), (256, 420), (266, 415), (272, 412), (277, 415), (283, 409), (291, 405), (297, 401), (305, 397), (313, 391), (318, 386), (321, 381), (328, 373), (334, 365), (337, 359), (344, 341), (351, 330), (352, 322), (356, 314), (360, 307), (365, 312), (373, 317), (382, 318), (383, 317), (390, 306), (391, 311), (404, 285), (403, 294), (415, 267), (422, 239), (424, 249), (432, 229), (432, 217), (428, 203), (424, 195), (429, 201), (427, 188), (423, 178), (430, 188), (428, 177), (424, 168), (421, 163), (412, 157), (406, 150), (397, 141), (391, 132), (390, 123), (394, 128), (386, 118), (371, 110), (365, 102), (355, 90), (363, 94), (353, 87), (335, 86), (322, 81), (333, 84), (323, 77), (314, 77), (302, 77), (295, 74), (304, 75), (281, 67), (269, 66), (254, 69), (244, 74), (247, 71), (240, 74), (233, 74), (230, 74), (223, 71), (231, 70), (225, 69), (214, 69), (207, 73), (202, 78), (198, 83), (193, 93), (185, 120), (190, 87), (181, 105), (179, 111), (174, 142), (171, 132), (168, 138), (174, 156), (161, 205), (157, 208), (157, 211), (156, 221), (158, 214), (177, 215), (206, 162)]
        self.l_glass = [(172, 224), (167, 232), (164, 243), (163, 255), (164, 263), (167, 269), (173, 275), (180, 279), (188, 281), (199, 281), (207, 279), (213, 276), (
            217, 271), (224, 261), (227, 251), (228, 244), (225, 238), (217, 233), (208, 229), (200, 226), (191, 223), (182, 221), (175, 222), (170, 225), (168, 230)]
        self.lips = [(190, 334), (196, 349), (225, 360), (239, 359), (254, 351), (254, 346), (244, 337), (214, 326), (195, 325), (188, 332), (191, 336), (198, 336), (208, 335),
                     (217, 338), (226, 339), (232, 342), (239, 345), (245, 347), (250, 347), (252, 348), (253, 352), (248, 352), (236, 350), (192, 338), (194, 344), (198, 350)]
        self.neck = [(149, 349), (144, 358), (142, 370), (144, 377), (146, 387), (150, 397), (152, 404), (154, 418), (156, 433), (157, 450), (158, 462), (162, 471), (168, 479), (176, 485), (178, 494), (187, 514), (186, 518), (186, 521), (189, 523), (193, 529), (196, 539), (204, 559), (231, 596), (243, 641), (275, 546),
                     (282, 531), (300, 514), (297, 493), (297, 485), (299, 477), (299, 473), (294, 472), (294, 465), (289, 456), (281, 443), (301, 409), (310, 391), (298, 400), (278, 408), (259, 415), (236, 421), (209, 418), (190, 408), (172, 391), (168, 381), (158, 368), (154, 358), (149, 349), (147, 355), (143, 362)]
        self.teeth = [(201, 337), (213, 342), (214, 337), (203, 335), (201, 337), (226, 347), (228, 346), (230, 341),
                      (235, 343), (233, 347), (228, 346), (229, 342), (237, 344), (238, 348), (240, 349), (243, 347), (237, 344)]
        self.inner_beard = [(201, 380), (198, 381), (195, 383), (193, 384), (191, 386), (187, 386), (186, 383), (184, 381), (182, 380), (179, 380), (179, 378), (178, 375), (178, 371), (176, 369), (178, 365), (178, 364), (179, 360), (179, 358), (179, 355), (179, 354), (182, 350), (182, 348), (182, 345), (182, 344), (184, 342), (186, 340), (186, 337), (187, 336), (190, 331), (193, 334), (193, 330), (196, 333), (196, 328), (198, 331), (200, 328), (201, 331), (202, 327), (207, 330), (207, 326), (208, 329), (210, 326), (211, 330), (213, 325), (214, 331), (217, 328), (219, 333), (223, 327), (223, 333), (224, 329), (224, 334), (228, 331), (227, 336), (229, 333), (230, 336), (232, 332), (232, 335), (234, 332), (232, 337), (236, 335), (236, 338), (238, 335), (238, 338), (243, 338), (239, 340), (244, 338), (242, 341), (248, 341), (246, 342), (250, 343), (247, 345), (249, 345), (252, 346), (253, 349), (256, 353), (
            256, 350), (258, 353), (258, 361), (258, 365), (259, 368), (253, 378), (257, 377), (252, 380), (252, 390), (249, 390), (249, 394), (247, 394), (246, 395), (243, 396), (242, 394), (241, 398), (238, 395), (238, 397), (236, 394), (235, 398), (235, 395), (231, 398), (231, 392), (229, 395), (226, 389), (226, 391), (222, 387), (218, 381), (216, 386), (216, 380), (220, 378), (221, 375), (223, 376), (224, 372), (226, 376), (228, 371), (229, 374), (231, 370), (232, 372), (232, 366), (230, 364), (221, 363), (203, 357), (201, 354), (196, 359), (195, 362), (199, 359), (197, 363), (200, 362), (197, 366), (200, 364), (199, 367), (201, 367), (200, 372), (202, 368), (200, 377), (202, 374), (200, 380), (194, 385), (193, 383), (188, 385), (188, 384), (186, 383), (182, 380), (177, 378), (176, 368), (178, 365), (178, 361), (179, 358), (178, 357), (179, 350), (182, 347), (182, 344), (185, 341), (189, 335), (189, 329)]
        self.r_glass = [(272, 249), (262, 252), (258, 259), (256, 264), (254, 272), (254, 280), (256, 289), (260, 298), (263, 301), (271, 307), (276, 309), (283, 311), (289, 312), (296, 313), (
            301, 311), (308, 306), (313, 299), (319, 289), (321, 282), (323, 274), (322, 270), (319, 266), (310, 260), (299, 255), (292, 252), (278, 249), (273, 249), (267, 250), (263, 251), (260, 254)]
        self.face = [(156, 220), (159, 214), (178, 215), (205, 163), (209, 157), (211, 155), (217, 155), (229, 157), (256, 164), (251, 165), (259, 171), (253, 170), (259, 175), (253, 175), (256, 177), (251, 179), (257, 182), (271, 182), (265, 180), (275, 180), (267, 175), (278, 179), (272, 173), (301, 180), (313, 187), (310, 178), (316, 181), (324, 186), (325, 183), (334, 190), (347, 198), (353, 203), (353, 210), (350, 216), (346, 227), (341, 238), (340, 243), (337, 255), (339, 266), (341, 254), (342, 266), (343, 261), (348, 259), (350, 260), (350, 270), (348, 278), (351, 275), (351, 279), (353, 278), (354, 280), (354, 282), (356, 279), (357, 284), (358, 281), (358, 285), (357, 286), (356, 295), (355, 291), (354, 293), (353, 299), (351, 296), (350, 300), (350, 309), (348, 305), (348, 312), (347, 314), (346, 318), (345, 315), (344, 321), (343, 330), (341, 337), (333, 346), (327, 359), (327, 354), (325, 359), (324, 356), (319, 361), (321, 355), (316, 361), (316, 356), (313, 361), (314, 353), (307, 361), (311, 353), (305, 359), (306, 353), (290, 370), (294, 364), (278, 380), (275, 382), (268, 384), (266, 380), (266, 369), (269, 364), (273, 357), (274, 351), (272, 343), (267, 332), (266, 335), (262, 331), (262, 333), (258, 327), (258, 329), (255, 325), (255, 328), (251, 322), (250, 324), (246, 321), (246, 323), (241, 319), (238, 317), (232, 315), (228, 319), (222, 317), (220, 313), (217, 309), (210, 309), (203, 308), (203, 310), (194, 312), (187, 313), (181, 316), (177, 321), (174, 329), (172, 335), (172, 344), (175, 341), (167, 351), (162, 344), (162, 337), (160, 341), (160, 333), (158, 336), (157, 329), (155, 321), (153, 313), (150, 307), (150, 300), (150, 291)]
        self.pen = tu.Turtle()
        self.turt = tu
        self.pen.speed(0)
        self.x_offset = x_offset
        self.y_offset = y_offset

    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset, (y*-1)+self.y_offset)
        self.pen.pendown()

    def paint(self, coord, co=(0, 0, 0)):
        self.pen.color(co)
        t_x, t_y = coord[0]
        self.go(t_x, t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            # print(i)
            x, y = i
            if t:
                self.go(x, y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset, (y*-1)+self.y_offset)
        self.pen.end_fill()

    def draw_fn(self, coord, mode=1, co=(0, 0, 0), thickness=1):
        co = (co[0]/255, co[1]/255, co[2]/255)

        self.pen.color(co)

        if mode:
            self.pen.width(thickness)
            t_x, t_y = coord[0]
            self.go(t_x, t_y)
            t = 0
            for i in coord[1:]:
                # print(i)
                x, y = i
                if t:
                    self.go(x, y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset, (y*-1)+self.y_offset)
        else:
            self.paint(coord=coord, co=co)

    def draw(self, retain=True):
        self.draw_fn(self.neck, co=(247, 164, 130), mode=0)
        self.draw_fn(self.dress, co=(75, 91, 153), mode=0)
        self.draw_fn(self.hair, co=(0, 0, 0), mode=0)
        self.draw_fn(self.face, co=(241, 152, 112), mode=0)
        self.draw_fn(self.glass_frame, co=(56, 53, 48), mode=0)
        self.draw_fn(self.l_glass, co=(7, 96, 148), mode=0)
        self.draw_fn(self.r_glass, co=(7, 96, 148), mode=0)
        self.draw_fn(self.inner_beard, co=(241, 152, 112), mode=0)
        self.draw_fn(self.lips, co=(238, 104, 114), mode=0)
        self.draw_fn(self.teeth, co=(0, 0, 0), mode=0)
        if retain:
            self.turt.done()


if __name__ == "__main__":
    tu.setup(1000, 1000)
    vijay = VIJAY()
    vijay.draw()
