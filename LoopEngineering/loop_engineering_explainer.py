from manim import *

class LoopEngineeringExplainer(Scene):
    def construct(self):
        # Palette configuration (White canvas, vibrant colorful elements)
        BG_COLOR = "#FFFFFF"
        BOX_BORDER = "#334155"       # dark slate, crisp on white
        BOX_FILL = "#F8FAFC"         # very light gray fill
        TEXT_COLOR = "#1E293B"       # near-black
        MUTED_TEXT = "#64748B"       # muted gray
        
        # Colors representing states
        GREEN_COLOR = "#059669"      # positive/refine
        RED_COLOR = "#DC2626"        # negative/vague
        BLUE_COLOR = "#2563EB"       # AI/Loop
        ORANGE_COLOR = "#EA580C"     # output/orange
        
        self.camera.background_color = BG_COLOR
        
        # --- Caption Setup ---
        caption_box = RoundedRectangle(
            width=12, height=1.3, corner_radius=0.15,
            stroke_color=BOX_BORDER, stroke_width=1.5,
            fill_color="#F8FAFC", fill_opacity=0.95
        ).to_edge(DOWN, buff=0.4)
        
        caption_text = Paragraph(
            "", font_size=18, font="Sans", color=TEXT_COLOR, line_spacing=0.5
        )
        
        caption_group = VGroup(caption_box, caption_text)
        self.add(caption_box)
        
        def play_caption(new_text, wait_time=2.0):
            nonlocal caption_text
            self.play(FadeOut(caption_text, run_time=0.15))
            caption_text = Paragraph(
                new_text, font_size=18, font="Sans", color=TEXT_COLOR,
                line_spacing=0.5, alignment="center"
            ).move_to(caption_box.get_center())
            self.play(FadeIn(caption_text, run_time=0.15))
            if wait_time > 0:
                self.wait(wait_time)

        # =========================================================================
        # 1. HOOK (0:00 - 12.84s)
        # =========================================================================
        split_line = Line(start=UP * 3, end=DOWN * 1.5, color=BOX_BORDER, stroke_width=1)
        self.play(Create(split_line))
        
        # Left: Prompt Engineering
        pe_title = Text("Prompt Engineering", font_size=20, color=TEXT_COLOR, weight=BOLD).shift(LEFT * 3 + UP * 2.2)
        pe_box = RoundedRectangle(
            width=3.2, height=2.2, corner_radius=0.15,
            stroke_color=RED_COLOR, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        ).shift(LEFT * 3 + UP * 0.4)
        pe_text = Paragraph(
            "Write the perfect\ninstruction upfront...",
            font_size=12, font="Sans", color=MUTED_TEXT, alignment="center"
        ).move_to(pe_box.get_center())
        frustrated_face = Text("🤬", font_size=32).next_to(pe_box, DOWN, buff=0.2)
        pe_group = VGroup(pe_title, pe_box, pe_text, frustrated_face)
        
        # Right: Loop Engineering
        le_title = Text("Loop Engineering", font_size=20, color=BLUE_COLOR, weight=BOLD).shift(RIGHT * 3 + UP * 2.2)
        le_box = RoundedRectangle(
            width=3.2, height=2.2, corner_radius=0.15,
            stroke_color=GREEN_COLOR, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        ).shift(RIGHT * 3 + UP * 0.4)
        
        # Curved loop arrows inside le_box
        arrow1 = CurvedArrow(
            start_point=le_box.get_center() + LEFT * 0.6 + UP * 0.15,
            end_point=le_box.get_center() + RIGHT * 0.6 + UP * 0.15,
            angle=-PI/2, color=GREEN_COLOR, stroke_width=4
        )
        arrow2 = CurvedArrow(
            start_point=le_box.get_center() + RIGHT * 0.6 + DOWN * 0.15,
            end_point=le_box.get_center() + LEFT * 0.6 + DOWN * 0.15,
            angle=-PI/2, color=GREEN_COLOR, stroke_width=4
        )
        loop_icon = VGroup(arrow1, arrow2)
        calm_icon = Text("🧠", font_size=32).next_to(le_box, DOWN, buff=0.2)
        le_group = VGroup(le_title, le_box, loop_icon, calm_icon)
        
        self.play(
            FadeIn(pe_group, shift=RIGHT),
            FadeIn(le_group, shift=LEFT)
        )
        
        play_caption(
            "Everyone's obsessed with writing the 'perfect prompt.'\nBut the best AI users don't do that.",
            wait_time=5.0
        )
        
        play_caption(
            "They do something called Loop Engineering —\nand it's way more powerful.",
            wait_time=5.3
        )

        # =========================================================================
        # 2. THE OLD WAY: PROMPT ENGINEERING (12.84 - 28.87s)
        # =========================================================================
        self.play(
            FadeOut(split_line),
            FadeOut(le_group),
            pe_group.animate.move_to(UP * 0.8).scale(1.2),
            run_time=1.0
        )
        
        prompt_box = RoundedRectangle(
            width=2.5, height=1.0, corner_radius=0.1,
            stroke_color=BOX_BORDER, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        ).shift(LEFT * 2 + UP * 0.5)
        prompt_label = Text("Ideal Prompt", font_size=14, color=TEXT_COLOR, weight=BOLD).move_to(prompt_box.get_center())
        
        flow_arrow = Arrow(start=prompt_box.get_right(), end=prompt_box.get_right() + RIGHT * 1.5, color=BOX_BORDER, stroke_width=3)
        
        output_box = RoundedRectangle(
            width=2.5, height=1.0, corner_radius=0.1,
            stroke_color=BOX_BORDER, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        ).shift(RIGHT * 2 + UP * 0.5)
        output_label = Text("One-Shot Output", font_size=14, color=TEXT_COLOR).move_to(output_box.get_center())
        
        self.play(
            ReplacementTransform(pe_box, prompt_box),
            ReplacementTransform(pe_text, prompt_label),
            FadeOut(pe_title),
            FadeOut(frustrated_face),
            Create(flow_arrow),
            FadeIn(output_box),
            FadeIn(output_label),
            run_time=1.2
        )
        
        play_caption(
            "Prompt engineering says: craft the ideal instruction upfront,\nget the perfect output in one shot.",
            wait_time=4.8
        )
        
        # Custom Cross
        line1 = Line(start=output_box.get_corner(UL), end=output_box.get_corner(DR), color=RED_COLOR, stroke_width=6)
        line2 = Line(start=output_box.get_corner(DL), end=output_box.get_corner(UR), color=RED_COLOR, stroke_width=6)
        red_cross = VGroup(line1, line2)
        wrong_label = Text("Often wrong or incomplete", font_size=14, color=RED_COLOR, weight=BOLD).next_to(output_box, DOWN, buff=0.3)
        
        self.play(
            Create(red_cross),
            FadeIn(wrong_label, shift=UP),
            run_time=1.0
        )
        
        play_caption(
            "Sounds efficient — but real problems are messy.\nYou can't predict everything you need in a single prompt.",
            wait_time=7.0
        )
        
        self.play(
            FadeOut(prompt_box),
            FadeOut(prompt_label),
            FadeOut(flow_arrow),
            FadeOut(output_box),
            FadeOut(output_label),
            FadeOut(red_cross),
            FadeOut(wrong_label),
            run_time=1.0
        )

        # =========================================================================
        # 3. THE LOOP: WHAT IT ACTUALLY LOOKS LIKE (28.87 - 47.23s)
        # =========================================================================
        node_w = 2.0
        node_h = 0.9
        
        prompt_pos = UP * 1.6 + LEFT * 2.5
        output_pos = UP * 1.6 + RIGHT * 2.5
        review_pos = DOWN * 0.8 + RIGHT * 2.5
        refine_pos = DOWN * 0.8 + LEFT * 2.5
        
        n_prompt = RoundedRectangle(width=node_w, height=node_h, corner_radius=0.1, stroke_color=BLUE_COLOR, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1).move_to(prompt_pos)
        t_prompt = Text("1. Prompt", font_size=14, color=BLUE_COLOR, weight=BOLD).move_to(prompt_pos)
        g_prompt = VGroup(n_prompt, t_prompt)
        
        n_output = RoundedRectangle(width=node_w, height=node_h, corner_radius=0.1, stroke_color=ORANGE_COLOR, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1).move_to(output_pos)
        t_output = Text("2. Output", font_size=14, color=ORANGE_COLOR, weight=BOLD).move_to(output_pos)
        g_output = VGroup(n_output, t_output)
        
        n_review = RoundedRectangle(width=node_w, height=node_h, corner_radius=0.1, stroke_color=MUTED_TEXT, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1).move_to(review_pos)
        t_review = Text("3. Review", font_size=14, color=MUTED_TEXT, weight=BOLD).move_to(review_pos)
        g_review = VGroup(n_review, t_review)
        
        n_refine = RoundedRectangle(width=node_w, height=node_h, corner_radius=0.1, stroke_color=GREEN_COLOR, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1).move_to(refine_pos)
        t_refine = Text("4. Refine", font_size=14, color=GREEN_COLOR, weight=BOLD).move_to(refine_pos)
        g_refine = VGroup(n_refine, t_refine)
        
        arr_p_to_o = CurvedArrow(start_point=prompt_pos + RIGHT * 1.1 + UP * 0.1, end_point=output_pos + LEFT * 1.1 + UP * 0.1, angle=-0.2, color=BOX_BORDER, stroke_width=2)
        arr_o_to_v = CurvedArrow(start_point=output_pos + DOWN * 0.55 + RIGHT * 0.1, end_point=review_pos + UP * 0.55 + RIGHT * 0.1, angle=-0.2, color=BOX_BORDER, stroke_width=2)
        arr_v_to_f = CurvedArrow(start_point=review_pos + LEFT * 1.1 + DOWN * 0.1, end_point=refine_pos + RIGHT * 1.1 + DOWN * 0.1, angle=-0.2, color=BOX_BORDER, stroke_width=2)
        arr_f_to_p = CurvedArrow(start_point=refine_pos + UP * 0.55 + LEFT * 0.1, end_point=prompt_pos + DOWN * 0.55 + LEFT * 0.1, angle=-0.2, color=BOX_BORDER, stroke_width=2)
        
        loop_arrows = VGroup(arr_p_to_o, arr_o_to_v, arr_v_to_f, arr_f_to_p)
        loop_nodes = VGroup(g_prompt, g_output, g_review, g_refine)
        loop_diagram = VGroup(loop_nodes, loop_arrows)
        
        self.play(
            FadeIn(loop_nodes, scale=0.9),
            Create(loop_arrows),
            run_time=1.5
        )
        
        self.play(
            g_prompt.animate.scale(1.15),
            arr_p_to_o.animate.set_stroke(color=BLUE_COLOR, width=4),
            run_time=0.8
        )
        self.play(
            g_output.animate.scale(1.15),
            arr_o_to_v.animate.set_stroke(color=ORANGE_COLOR, width=4),
            run_time=0.8
        )
        
        play_caption(
            "Loop Engineering flips it: write a rough prompt, get a rough output...",
            wait_time=3.5
        )
        
        self.play(
            g_review.animate.scale(1.15).set_color(RED_COLOR),
            arr_v_to_f.animate.set_stroke(color=RED_COLOR, width=4),
            run_time=0.8
        )
        self.play(
            g_refine.animate.scale(1.15),
            arr_f_to_p.animate.set_stroke(color=GREEN_COLOR, width=4),
            run_time=0.8
        )
        
        play_caption(
            "...look at what's wrong, tell the AI exactly that — and repeat.",
            wait_time=3.2
        )
        
        self.play(
            g_prompt.animate.scale(1.0/1.15),
            g_output.animate.scale(1.0/1.15),
            g_review.animate.scale(1.0/1.15),
            g_refine.animate.scale(1.0/1.15),
            run_time=0.8
        )
        
        play_caption(
            "Each pass gets sharper. You're not guessing the perfect input.\nYou're steering with feedback.",
            wait_time=7.5
        )

        # =========================================================================
        # 4. WHY THIS WORKS BETTER (47.23 - 64.65s)
        # =========================================================================
        self.play(
            loop_diagram.animate.scale(0.65).move_to(LEFT * 3.8 + UP * 0.5),
            run_time=1.0
        )
        
        why_title = Text("How Feedback Works", font_size=18, color=TEXT_COLOR, weight=BOLD).move_to(RIGHT * 2.2 + UP * 2.2)
        self.play(FadeIn(why_title), run_time=0.5)
        
        vague_box = RoundedRectangle(
            width=4.0, height=0.9, corner_radius=0.1,
            stroke_color=MUTED_TEXT, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        ).move_to(RIGHT * 2.2 + UP * 1.0)
        vague_text = Paragraph(
            '❌ Vague: "Make it better"\n(AI guesses, usually fails)',
            font_size=12, font="Sans", color=RED_COLOR, alignment="center"
        ).move_to(vague_box.get_center())
        vague_bubble = VGroup(vague_box, vague_text)
        
        self.play(FadeIn(vague_bubble, shift=DOWN), run_time=0.8)
        
        play_caption(
            "This works because AI is bad at reading your mind,\nbut great at reacting to specifics. 'Make it better' fails.",
            wait_time=7.5
        )
        
        specific_box = RoundedRectangle(
            width=4.0, height=1.1, corner_radius=0.1,
            stroke_color=GREEN_COLOR, stroke_width=2.5,
            fill_color=BOX_FILL, fill_opacity=1
        ).move_to(RIGHT * 2.2 + DOWN * 0.5)
        specific_text = Paragraph(
            '✅ Specific: "This section is too long,\ncut it to two sentences."\n(Concrete target)',
            font_size=12, font="Sans", color=GREEN_COLOR, alignment="center"
        ).move_to(specific_box.get_center())
        specific_bubble = VGroup(specific_box, specific_text)
        
        self.play(FadeIn(specific_bubble, shift=UP), run_time=0.8)
        
        play_caption(
            "...'This section is too long, cut it to two sentences' works —\nbecause now the AI has a concrete target.",
            wait_time=7.0
        )
        
        self.play(
            FadeOut(vague_bubble),
            FadeOut(specific_bubble),
            FadeOut(why_title),
            run_time=1.0
        )

        # =========================================================================
        # 5. THE PRACTICAL VERSION (64.65 - 82.72s)
        # =========================================================================
        compare_title = Text("Which path is faster?", font_size=18, color=TEXT_COLOR, weight=BOLD).move_to(RIGHT * 2.2 + UP * 2.2)
        self.play(FadeIn(compare_title), run_time=0.5)
        
        slow_box = RoundedRectangle(
            width=2.1, height=2.2, corner_radius=0.1,
            stroke_color=RED_COLOR, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        ).move_to(RIGHT * 0.9 + UP * 0.4)
        slow_label = Text("One Slow Try", font_size=12, color=MUTED_TEXT, weight=BOLD).move_to(slow_box.get_top() + DOWN * 0.3)
        slow_time = Text("10 Mins", font_size=20, color=RED_COLOR, weight=BOLD).next_to(slow_label, DOWN, buff=0.2)
        slow_result = Paragraph("Mediocre\nResult ❌", font_size=10, color=RED_COLOR, alignment="center").next_to(slow_time, DOWN, buff=0.2)
        slow_group = VGroup(slow_box, slow_label, slow_time, slow_result)
        
        fast_box = RoundedRectangle(
            width=2.1, height=2.2, corner_radius=0.1,
            stroke_color=GREEN_COLOR, stroke_width=2.5,
            fill_color=BOX_FILL, fill_opacity=1
        ).move_to(RIGHT * 3.5 + UP * 0.4)
        fast_label = Text("3 Quick Loops", font_size=12, color=BLUE_COLOR, weight=BOLD).move_to(fast_box.get_top() + DOWN * 0.3)
        fast_time = Text("3 Mins", font_size=20, color=GREEN_COLOR, weight=BOLD).next_to(fast_label, DOWN, buff=0.2)
        fast_result = Paragraph("Sharp\nResult ✅", font_size=10, color=GREEN_COLOR, alignment="center").next_to(fast_time, DOWN, buff=0.2)
        fast_group = VGroup(fast_box, fast_label, fast_time, fast_result)
        
        self.play(
            FadeIn(slow_group, shift=RIGHT),
            run_time=0.8
        )
        
        play_caption(
            "In practice: don't spend 10 minutes perfecting your first prompt.\nSpend 30 seconds on a rough one...",
            wait_time=7.5
        )
        
        self.play(
            FadeIn(fast_group, shift=LEFT),
            Flash(fast_box.get_center(), color=GREEN_COLOR, line_length=0.15, flash_radius=0.6),
            run_time=1.0
        )
        
        play_caption(
            "...then spend your time reacting — that's where the real quality comes from.\nThree fast loops beat one slow, perfect attempt.",
            wait_time=8.2
        )
        
        self.play(
            FadeOut(slow_group),
            FadeOut(fast_group),
            FadeOut(compare_title),
            run_time=1.0
        )

        # =========================================================================
        # 6. CLOSER (82.72 - 88.31s)
        # =========================================================================
        self.play(
            loop_diagram.animate.scale(1.0/0.65).move_to(UP * 0.4),
            run_time=1.0
        )
        
        self.play(
            loop_diagram.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.2
        )
        
        play_caption(
            "Stop engineering the perfect prompt. Start engineering the loop.",
            wait_time=1.5
        )
        
        final_title = Text("Loop Engineering", font_size=36, color=GREEN_COLOR, weight=BOLD).move_to(UP * 0.8)
        final_vs = Text(">", font_size=40, color=MUTED_TEXT, weight=BOLD).next_to(final_title, DOWN, buff=0.2)
        final_subtitle = Text("Prompt Engineering", font_size=28, color=RED_COLOR, weight=BOLD).next_to(final_vs, DOWN, buff=0.2)
        final_card = VGroup(final_title, final_vs, final_subtitle)
        
        self.play(
            FadeOut(loop_diagram),
            FadeIn(final_card, scale=0.8),
            run_time=1.2
        )
        self.wait(1.0)

        # =========================================================================
        # 7. CALL TO ACTION (CTA) (88.31 - 95.80s)
        # =========================================================================
        play_caption("If you found this helpful, please like, share, and subscribe.\nSee you in the next one!", wait_time=0.0)

        # Shift final card up to make room
        self.play(final_card.animate.shift(UP * 0.7), run_time=0.8)

        # Create buttons
        # Like Button
        like_box = RoundedRectangle(
            width=1.8, height=0.6, corner_radius=0.1,
            stroke_color=BOX_BORDER, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        )
        like_label = Text("👍 Like", font_size=12, color=TEXT_COLOR, weight=BOLD).move_to(like_box.get_center())
        like_btn = VGroup(like_box, like_label)

        # Share Button
        share_box = RoundedRectangle(
            width=1.8, height=0.6, corner_radius=0.1,
            stroke_color=BOX_BORDER, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        )
        share_label = Text("🔗 Share", font_size=12, color=TEXT_COLOR, weight=BOLD).move_to(share_box.get_center())
        share_btn = VGroup(share_box, share_label)

        # Subscribe Button
        sub_box = RoundedRectangle(
            width=2.2, height=0.6, corner_radius=0.1,
            stroke_color=RED_COLOR, stroke_width=2,
            fill_color=RED_COLOR, fill_opacity=1
        )
        sub_label = Text("Subscribe", font_size=12, color=WHITE, weight=BOLD).move_to(sub_box.get_center())
        sub_btn = VGroup(sub_box, sub_label)

        cta_buttons = VGroup(like_btn, share_btn, sub_btn).arrange(RIGHT, buff=0.4).shift(DOWN * 0.8)

        self.play(FadeIn(cta_buttons, shift=UP), run_time=0.8)

        # Add cursor (custom drawn arrow pointing up-left)
        cursor_poly = Polygon(
            ORIGIN, DOWN * 0.4 + RIGHT * 0.1, DOWN * 0.25 + RIGHT * 0.18, 
            DOWN * 0.35 + RIGHT * 0.32, DOWN * 0.3 + RIGHT * 0.35, 
            DOWN * 0.2 + RIGHT * 0.2, DOWN * 0.25 + RIGHT * 0.3,
            color=TEXT_COLOR, fill_color=TEXT_COLOR, fill_opacity=1
        ).scale(0.8)
        cursor = VGroup(cursor_poly).move_to(RIGHT * 4.5 + DOWN * 3)
        self.play(FadeIn(cursor), run_time=0.4)

        # 1. Animate clicking LIKE
        self.play(cursor.animate.move_to(like_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(
            like_box.animate.scale(0.92), 
            like_label.animate.scale(0.92),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        self.play(
            like_box.animate.scale(1.0/0.92).set_fill(color=BLUE_COLOR).set_stroke(color=BLUE_COLOR),
            like_label.animate.scale(1.0/0.92).set_color(color=WHITE),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(like_box.get_center(), color=BLUE_COLOR, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 2. Animate clicking SUBSCRIBE
        self.play(cursor.animate.move_to(sub_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(
            sub_box.animate.scale(0.92),
            sub_label.animate.scale(0.92),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        new_sub_label = Text("Subscribed", font_size=12, color="#475569", weight=BOLD).move_to(sub_box.get_center())
        self.play(
            sub_box.animate.scale(1.0/0.92).set_fill(color="#E2E8F0").set_stroke(color="#CBD5E1"),
            ReplacementTransform(sub_label, new_sub_label),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(sub_box.get_center(), color=RED_COLOR, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 3. Animate clicking SHARE
        self.play(cursor.animate.move_to(share_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(
            share_box.animate.scale(0.92),
            share_label.animate.scale(0.92),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        self.play(
            share_box.animate.scale(1.0/0.92).set_fill(color=GREEN_COLOR).set_stroke(color=GREEN_COLOR),
            share_label.animate.scale(1.0/0.92).set_color(color=WHITE),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(share_box.get_center(), color=GREEN_COLOR, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        self.play(
            cursor.animate.move_to(RIGHT * 4.5 + DOWN * 3),
            FadeOut(cursor),
            run_time=0.4
        )
        self.wait(1.8)
