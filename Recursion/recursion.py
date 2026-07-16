from manim import *
from manim.utils.rate_functions import ease_out_back

class Recursion(Scene):
    def construct(self):
        # Palette matching brand consistency
        BG_COLOR = "#FFFFFF"
        BOX_BORDER = "#334155"
        BOX_FILL = "#F1F5F9"
        BLUE = "#2563EB"       # still calling itself
        GREEN = "#059669"      # hit the base case
        AMBER = "#D97706"      # returning / unwinding
        RED = "#DC2626"        # danger / stack overflow
        TEXT_COLOR = "#1E293B"
        MUTED = "#64748B"

        self.camera.background_color = BG_COLOR

        # Add decorative grid lines for visual richness (faded background)
        grid = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": "#F1F5F9", "stroke_width": 1, "stroke_opacity": 0.5}
        )
        self.add(grid)

        # =========================================================================
        # 1. HOOK (0:00-0:11.04, duration = 11.04s)
        # =========================================================================
        hook_title = Text("Recursion", font_size=36, color=BLUE, weight=BOLD, font="Arial").move_to(UP * 2.5)
        
        # Draw three boxes in a horizontal row representing delegation of tasks
        # Box 1 (large, blue)
        doll1_shadow = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15, fill_color="#64748B", fill_opacity=0.15, stroke_width=0).move_to(LEFT * 3.8 + DOWN * 0.3 + DOWN * 0.05 + RIGHT * 0.05)
        doll1_box = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15, stroke_color=BLUE, stroke_width=3, fill_color=BOX_FILL, fill_opacity=1).move_to(LEFT * 3.8 + DOWN * 0.3)
        doll1_text = Text("solve(problem)", font_size=12, color=BLUE, weight=BOLD, font="Arial").move_to(doll1_box.get_center())
        doll1_group = VGroup(doll1_shadow, doll1_box, doll1_text)

        # Box 2 (medium, orange)
        doll2_shadow = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15, fill_color="#64748B", fill_opacity=0.15, stroke_width=0).move_to(DOWN * 0.3 + DOWN * 0.05 + RIGHT * 0.05)
        doll2_box = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15, stroke_color=AMBER, stroke_width=3, fill_color=BOX_FILL, fill_opacity=1).move_to(DOWN * 0.3)
        doll2_text = Text("solve(smaller)", font_size=12, color=AMBER, weight=BOLD, font="Arial").move_to(doll2_box.get_center())
        doll2_group = VGroup(doll2_shadow, doll2_box, doll2_text)

        # Box 3 (small, green)
        doll3_shadow = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15, fill_color="#64748B", fill_opacity=0.15, stroke_width=0).move_to(RIGHT * 3.8 + DOWN * 0.3 + DOWN * 0.05 + RIGHT * 0.05)
        doll3_box = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15, stroke_color=GREEN, stroke_width=3, fill_color=BOX_FILL, fill_opacity=1).move_to(RIGHT * 3.8 + DOWN * 0.3)
        doll3_text = Text("solve(tiny)", font_size=12, color=GREEN, weight=BOLD, font="Arial").move_to(doll3_box.get_center())
        doll3_group = VGroup(doll3_shadow, doll3_box, doll3_text)

        # Connectors
        a1 = CurvedArrow(doll1_box.get_right() + UP * 0.1, doll2_box.get_left() + UP * 0.1, angle=-TAU/8, color=MUTED, stroke_width=2.5)
        a2 = CurvedArrow(doll2_box.get_right() + UP * 0.1, doll3_box.get_left() + UP * 0.1, angle=-TAU/8, color=MUTED, stroke_width=2.5)

        self.play(
            FadeIn(hook_title, shift=DOWN * 0.3, rate_func=ease_out_back),
            FadeIn(doll1_group, scale=0.9, rate_func=ease_out_back),
            run_time=1.0
        )
        
        self.wait(3.0)

        # Step 2: Draw first curved arrow and slide energy dot from Box 1 to reveal Box 2
        flow_dot1 = Dot(color=BLUE, radius=0.08).move_to(a1.get_start())
        self.play(Create(a1), run_time=0.4)
        self.play(MoveAlongPath(flow_dot1, a1), run_time=0.3)
        self.play(
            FadeOut(flow_dot1), 
            FadeIn(doll2_group, scale=0.9, rate_func=ease_out_back), 
            run_time=0.4
        )
        
        self.wait(1.7)

        # Step 3: Draw second curved arrow and slide energy dot from Box 2 to reveal Box 3
        flow_dot2 = Dot(color=AMBER, radius=0.08).move_to(a2.get_start())
        self.play(Create(a2), run_time=0.4)
        self.play(MoveAlongPath(flow_dot2, a2), run_time=0.3)
        self.play(
            FadeOut(flow_dot2), 
            FadeIn(doll3_group, scale=0.9, rate_func=ease_out_back), 
            run_time=0.4
        )

        self.wait(1.74)

        self.play(
            FadeOut(hook_title),
            FadeOut(doll1_group),
            FadeOut(doll2_group),
            FadeOut(doll3_group),
            FadeOut(a1),
            FadeOut(a2),
            run_time=0.8
        )
        self.wait(0.6)

        # =========================================================================
        # 2. THE CORE IDEA (0:11.04-0:32.71, duration = 21.072s + 0.6s silence = 21.672s)
        # =========================================================================
        stair_title = Text("The Call Stack Stacked", font_size=18, color=TEXT_COLOR, weight=BOLD, font="Arial").move_to(UP * 2.8)
        self.play(FadeIn(stair_title), run_time=0.6)

        # Draw staircase steps building down from (-3.5, 2.0) to (3.5, -2.5)
        # Node width 2.0, height 0.5. Clear vertical gap = 0.9 - 0.5 = 0.4 units.
        def make_stair_node(label, pos, color=BLUE):
            shadow = RoundedRectangle(width=2.0, height=0.5, corner_radius=0.1, fill_color="#64748B", fill_opacity=0.12, stroke_width=0).move_to(pos + DOWN * 0.04 + RIGHT * 0.04)
            box = RoundedRectangle(width=2.0, height=0.5, corner_radius=0.1, stroke_color=color, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1).move_to(pos)
            text = Text(label, font_size=10, color=color, weight=BOLD, font="Arial").move_to(box.get_center())
            return VGroup(shadow, box, text)

        steps_num = [5, 4, 3, 2, 1]
        stair_nodes = VGroup()
        stair_arrows = VGroup()

        for i, n in enumerate(steps_num):
            pos = np.array([-3.5 + i * 1.4, 2.0 - i * 0.9, 0])
            node = make_stair_node(f"countdown({n})", pos, BLUE)
            stair_nodes.add(node)
            if i > 0:
                p1 = stair_nodes[i-1][1].get_bottom() + RIGHT * 0.3
                p2 = node[1].get_top() + LEFT * 0.3
                arrow = CurvedArrow(p1, p2, angle=-TAU/8, color=MUTED, stroke_width=2.0)
                stair_arrows.add(arrow)

        # Animate descent step-by-step with energy flow dots
        self.play(FadeIn(stair_nodes[0], scale=0.9, rate_func=ease_out_back), run_time=0.8)
        self.wait(4.0)

        # Step 1
        flow_dot1 = Dot(color=BLUE, radius=0.08).move_to(stair_arrows[0].get_start())
        self.play(Create(stair_arrows[0]), run_time=0.4)
        self.play(MoveAlongPath(flow_dot1, stair_arrows[0]), run_time=0.3)
        self.play(FadeOut(flow_dot1), FadeIn(stair_nodes[1], scale=0.9, rate_func=ease_out_back), run_time=0.4)
        self.wait(2.7) # Adjusted for timings

        # Step 2
        flow_dot2 = Dot(color=BLUE, radius=0.08).move_to(stair_arrows[1].get_start())
        self.play(Create(stair_arrows[1]), run_time=0.4)
        self.play(MoveAlongPath(flow_dot2, stair_arrows[1]), run_time=0.3)
        self.play(FadeOut(flow_dot2), FadeIn(stair_nodes[2], scale=0.9, rate_func=ease_out_back), run_time=0.4)
        self.wait(2.7)

        # Step 3 and 4 popping in sequentially
        flow_dot3 = Dot(color=BLUE, radius=0.08).move_to(stair_arrows[2].get_start())
        self.play(Create(stair_arrows[2]), run_time=0.3)
        self.play(MoveAlongPath(flow_dot3, stair_arrows[2]), run_time=0.25)
        self.play(FadeOut(flow_dot3), FadeIn(stair_nodes[3], scale=0.9, rate_func=ease_out_back), run_time=0.35)

        flow_dot4 = Dot(color=BLUE, radius=0.08).move_to(stair_arrows[3].get_start())
        self.play(Create(stair_arrows[3]), run_time=0.3)
        self.play(MoveAlongPath(flow_dot4, stair_arrows[3]), run_time=0.25)
        self.play(FadeOut(flow_dot4), FadeIn(stair_nodes[4], scale=0.9, rate_func=ease_out_back), run_time=0.35)

        self.wait(7.572)

        # =========================================================================
        # 3. THE BASE CASE (0:32.71-0:48.69, duration = 15.384s + 0.6s silence = 15.984s)
        # =========================================================================
        # Spawn the final base case: countdown(0) in GREEN with STOP badge and green Flash
        base_pos = np.array([-3.5 + 5 * 1.4, 2.0 - 5 * 0.9, 0])
        base_node = make_stair_node("countdown(0)", base_pos, GREEN)
        
        arrow_base = CurvedArrow(
            stair_nodes[4][1].get_bottom() + RIGHT * 0.3, 
            base_node[1].get_top() + LEFT * 0.3, 
            angle=-TAU/8, color=MUTED, stroke_width=2.0
        )

        stop_badge_shadow = RoundedRectangle(width=0.8, height=0.35, corner_radius=0.08, fill_color="#64748B", fill_opacity=0.12, stroke_width=0).next_to(base_node[1], RIGHT, buff=0.12).shift(DOWN * 0.03 + RIGHT * 0.03)
        stop_badge = RoundedRectangle(width=0.8, height=0.35, corner_radius=0.08, stroke_width=0, fill_color=GREEN, fill_opacity=1).next_to(base_node[1], RIGHT, buff=0.12)
        stop_text = Text("STOP", font_size=10, color=WHITE, weight=BOLD, font="Arial").move_to(stop_badge.get_center())
        stop_group = VGroup(stop_badge_shadow, stop_badge, stop_text)

        self.wait(4.0)

        # Energy flow dot for base case
        flow_dot_base = Dot(color=BLUE, radius=0.08).move_to(arrow_base.get_start())
        self.play(Create(arrow_base), run_time=0.4)
        self.play(MoveAlongPath(flow_dot_base, arrow_base), run_time=0.3)
        self.play(
            FadeOut(flow_dot_base),
            FadeIn(base_node, scale=0.9, rate_func=ease_out_back),
            Flash(base_node[1].get_center(), color=GREEN, line_length=0.2, flash_radius=0.4),
            run_time=0.4
        )
        
        self.wait(3.0)

        self.play(
            FadeIn(stop_group, scale=1.2, rate_func=ease_out_back),
            Flash(stop_badge.get_center(), color=GREEN, line_length=0.15, flash_radius=0.3),
            run_time=0.8
        )

        self.wait(6.784)

        # =========================================================================
        # 4. HOW IT UNWINDS (0:48.69-1:07.31, duration = 18.024s + 0.6s silence = 18.624s)
        # =========================================================================
        # Visualizing the stack unwinding bottom-to-top by lighting them up in AMBER
        unwind_arrows = [arrow_base, stair_arrows[3], stair_arrows[2], stair_arrows[1], stair_arrows[0]]
        unwind_nodes = [stair_nodes[4], stair_nodes[3], stair_nodes[2], stair_nodes[1], stair_nodes[0]]

        self.wait(2.0)

        # Step-by-step unwinding sequence moving in reverse (upwards)
        for i in range(5):
            arr = unwind_arrows[i]
            node = unwind_nodes[i]
            
            # Dot travels BACKWARDS along the arrow path (from end to start)
            ret_dot = Dot(color=AMBER, radius=0.08).move_to(arr.get_end())
            self.play(
                MoveAlongPath(ret_dot, arr, rate_func=lambda t: 1 - t), 
                run_time=0.4
            )
            
            # Turn the parent node AMBER with a soft flash
            amber_node = make_stair_node(node[2].text, node[1].get_center(), AMBER)
            self.play(
                FadeOut(ret_dot),
                Transform(node, amber_node),
                Flash(node[1].get_center(), color=AMBER, line_length=0.15, flash_radius=0.3),
                run_time=0.2
            )

        # Light up the entire staircase calmly in amber glow
        self.play(
            base_node.animate.scale(1.05),
            *[stair_nodes[j].animate.scale(1.05) for j in range(5)],
            run_time=0.5
        )
        self.play(
            base_node.animate.scale(1.0/1.05),
            *[stair_nodes[j].animate.scale(1.0/1.05) for j in range(5)],
            run_time=0.5
        )

        self.wait(11.224)

        # Clean screen for Section 5
        self.play(
            FadeOut(stair_title),
            FadeOut(stair_nodes),
            FadeOut(stair_arrows),
            FadeOut(base_node),
            FadeOut(arrow_base),
            FadeOut(stop_group),
            run_time=0.8
        )
        self.wait(0.6)

        # =========================================================================
        # 5. THE ONE RULE (1:07.31-1:20.15, duration = 12.240s + 0.6s silence = 12.840s)
        # =========================================================================
        rule_title = Text("The Infinite Loop Warning", font_size=18, color=TEXT_COLOR, weight=BOLD, font="Arial").move_to(UP * 2.8)
        self.play(FadeIn(rule_title), run_time=0.6)

        # Left: countdown(x) calling itself with same x
        err_box_shadow = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.15, fill_color="#64748B", fill_opacity=0.12, stroke_width=0).move_to(LEFT * 2.8 + DOWN * 0.05 + RIGHT * 0.05)
        err_box = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.15, stroke_color=RED, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1).move_to(LEFT * 2.8)
        err_text = Text("countdown(x)", font_size=14, color=RED, weight=BOLD, font="Arial").move_to(err_box.get_center() + UP * 0.25)
        err_sub = Text("calls countdown(x)", font_size=10, color=MUTED, font="Arial").move_to(err_box.get_center() + DOWN * 0.25)
        err_group = VGroup(err_box_shadow, err_box, err_text, err_sub)

        # Curved loop-back arrow
        loop_arrow = CurvedArrow(
            err_box.get_right() + UP * 0.2,
            err_box.get_right() + DOWN * 0.2,
            angle=1.5*PI, color=RED, stroke_width=3
        )

        self.play(
            FadeIn(err_group, scale=0.9, rate_func=ease_out_back),
            Create(loop_arrow),
            run_time=0.8
        )

        self.wait(4.0)

        # Stacking 6 red boxes vertically on the right to visualize stack overflow piling up
        stack_boxes = VGroup()
        for j in range(6):
            stack_pos = RIGHT * 2.8 + (DOWN * 2.0 + j * 0.72)
            stack_box_shadow = RoundedRectangle(width=3.0, height=0.5, corner_radius=0.1, fill_color="#64748B", fill_opacity=0.12, stroke_width=0).move_to(stack_pos + DOWN * 0.04 + RIGHT * 0.04)
            stack_box = RoundedRectangle(width=3.0, height=0.5, corner_radius=0.1, stroke_color=RED, stroke_width=2, fill_color="#FEF2F2", fill_opacity=1).move_to(stack_pos)
            stack_text = Text(f"countdown({5-j})", font_size=11, color=RED, weight=BOLD, font="Arial").move_to(stack_box.get_center())
            stack_boxes.add(VGroup(stack_box_shadow, stack_box, stack_text))

        # Pile them up rapidly
        for j in range(6):
            self.play(
                FadeIn(stack_boxes[j], shift=UP * 0.4, scale=0.9, rate_func=ease_out_back),
                run_time=0.15
            )

        # Play a visual shake & red Flash on overflow
        self.play(
            stack_boxes.animate.shift(LEFT * 0.1),
            err_group.animate.shift(LEFT * 0.05),
            rate_func=there_and_back,
            run_time=0.12
        )
        self.play(
            stack_boxes.animate.shift(RIGHT * 0.1),
            err_group.animate.shift(RIGHT * 0.05),
            rate_func=there_and_back,
            run_time=0.12
        )

        # STACK OVERFLOW badge flashes over the pile
        overflow_shadow = RoundedRectangle(width=4.2, height=1.6, corner_radius=0.15, fill_color="#64748B", fill_opacity=0.15, stroke_width=0).move_to(RIGHT * 2.8 + DOWN * 0.05 + RIGHT * 0.05)
        overflow_card = RoundedRectangle(width=4.2, height=1.6, corner_radius=0.15, stroke_color=RED, stroke_width=3, fill_color="#FEF2F2", fill_opacity=1).move_to(RIGHT * 2.8)
        overflow_title = Text("STACK OVERFLOW", font_size=16, color=RED, weight=BOLD, font="Arial").move_to(overflow_card.get_center() + UP * 0.3)
        overflow_sub = Text("out of memory error", font_size=11, color=TEXT_COLOR, font="Arial").move_to(overflow_card.get_center() + DOWN * 0.3)
        overflow_badge = VGroup(overflow_shadow, overflow_card, overflow_title, overflow_sub)

        self.play(
            FadeIn(overflow_badge, scale=0.92, rate_func=ease_out_back),
            Flash(overflow_card.get_center(), color=RED, line_length=0.25, flash_radius=0.5),
            run_time=0.6
        )

        self.wait(4.7) # Adjusted for timings

        self.play(
            FadeOut(rule_title),
            FadeOut(err_group),
            FadeOut(loop_arrow),
            FadeOut(stack_boxes),
            FadeOut(overflow_badge),
            run_time=0.8
        )
        self.wait(0.6)

        # =========================================================================
        # 6. CLOSER (1:20.15-1:29.10, duration = 8.352s + 0.6s silence = 8.952s)
        # =========================================================================
        # Premium Dashboard Card summary
        card_shadow = RoundedRectangle(width=8.5, height=4.2, corner_radius=0.25, fill_color="#64748B", fill_opacity=0.15, stroke_width=0).move_to(DOWN * 0.1 + DOWN * 0.08 + RIGHT * 0.08)
        card_bg = RoundedRectangle(width=8.5, height=4.2, corner_radius=0.25, stroke_color=BLUE, stroke_width=3.5, fill_color=BOX_FILL, fill_opacity=1).move_to(DOWN * 0.1)
        card_title = Text("Recursion: The Three Rules", font_size=20, color=TEXT_COLOR, weight=BOLD, font="Arial").move_to(card_bg.get_center() + UP * 1.5)
        
        # Rule rows
        r1_pill = RoundedRectangle(width=1.8, height=0.45, corner_radius=0.08, stroke_width=0, fill_color="#EFF6FF", fill_opacity=1).move_to(card_bg.get_center() + LEFT * 2.5 + UP * 0.6)
        r1_label = Text("1. DIVIDE", font_size=11, color=BLUE, weight=BOLD, font="Arial").move_to(r1_pill.get_center())
        r1_desc = Text("Solve a smaller version of the same problem.", font_size=12, color=TEXT_COLOR, font="Arial").next_to(r1_pill, RIGHT, buff=0.4)
        
        r2_pill = RoundedRectangle(width=1.8, height=0.45, corner_radius=0.08, stroke_width=0, fill_color="#ECFDF5", fill_opacity=1).move_to(card_bg.get_center() + LEFT * 2.5 + DOWN * 0.1)
        r2_label = Text("2. STOP", font_size=11, color=GREEN, weight=BOLD, font="Arial").move_to(r2_pill.get_center())
        r2_desc = Text("Define a base case to halt recursion cleanly.", font_size=12, color=TEXT_COLOR, font="Arial").next_to(r2_pill, RIGHT, buff=0.4)
        
        r3_pill = RoundedRectangle(width=1.8, height=0.45, corner_radius=0.08, stroke_width=0, fill_color="#FEF3C7", fill_opacity=1).move_to(card_bg.get_center() + LEFT * 2.5 + DOWN * 0.8)
        r3_label = Text("3. UNWIND", font_size=11, color=AMBER, weight=BOLD, font="Arial").move_to(r3_pill.get_center())
        r3_desc = Text("Let the answers build back up the call stack.", font_size=12, color=TEXT_COLOR, font="Arial").next_to(r3_pill, RIGHT, buff=0.4)
        
        final_card = VGroup(
            card_shadow, card_bg, card_title,
            r1_pill, r1_label, r1_desc,
            r2_pill, r2_label, r2_desc,
            r3_pill, r3_label, r3_desc
        )

        self.play(
            FadeIn(final_card, scale=0.85, rate_func=ease_out_back),
            run_time=1.2
        )
        self.wait(7.152)

        # =========================================================================
        # 7. CALL TO ACTION (CTA) (1:29.10-1:36.59, duration = 7.488s)
        # =========================================================================
        # Slide final card up and scale down
        self.play(final_card.animate.to_edge(UP, buff=0.5).scale(0.75), run_time=0.8)

        # --- SUBSCRIBE BUTTON ---
        sub_btn_box = RoundedRectangle(width=5.5, height=1.1, corner_radius=0.15, stroke_width=0, fill_color=RED, fill_opacity=1)
        yt_icon_box = RoundedRectangle(width=0.8, height=0.55, corner_radius=0.12, stroke_width=0, fill_color=WHITE, fill_opacity=1)
        yt_triangle = Triangle(color=RED, fill_color=RED, fill_opacity=1).scale(0.12).rotate(-PI/2).move_to(yt_icon_box.get_center())
        yt_logo = VGroup(yt_icon_box, yt_triangle)
        sub_text = Text("SUBSCRIBE", font_size=24, color=WHITE, weight=BOLD, font="Arial")
        
        # Bell icon
        bell_body = Arc(radius=0.22, start_angle=0, angle=PI, color=WHITE, stroke_width=0, fill_color=WHITE, fill_opacity=1)
        bell_base = RoundedRectangle(width=0.55, height=0.08, corner_radius=0.02, stroke_width=0, fill_color=WHITE, fill_opacity=1).next_to(bell_body, DOWN, buff=0.02)
        bell_clapper = Circle(radius=0.07, color=WHITE, stroke_width=0, fill_color=WHITE, fill_opacity=1).next_to(bell_base, DOWN, buff=0.02)
        bell_icon = VGroup(bell_body, bell_base, bell_clapper)
        
        sub_button_contents = VGroup(yt_logo, sub_text, bell_icon).arrange(RIGHT, buff=0.4)
        sub_button = VGroup(sub_btn_box, sub_button_contents).move_to(DOWN * 0.1)

        # --- LOWER CTA ICONS ---
        like_icon = Text("👍", font_size=28)
        like_label = Text("Like", font_size=14, color=TEXT_COLOR, font="Arial").next_to(like_icon, DOWN, buff=0.15)
        like_btn = VGroup(like_icon, like_label)
        
        comment_icon = Text("💬", font_size=28)
        comment_label = Text("Comment", font_size=14, color=TEXT_COLOR, font="Arial").next_to(comment_icon, DOWN, buff=0.15)
        comment_btn = VGroup(comment_icon, comment_label)
        
        share_icon = Text("🔗", font_size=28)
        share_label = Text("Share", font_size=14, color=TEXT_COLOR, font="Arial").next_to(share_icon, DOWN, buff=0.15)
        share_btn = VGroup(share_icon, share_label)
        
        cta_icons = VGroup(like_btn, comment_btn, share_btn).arrange(RIGHT, buff=1.2).next_to(sub_button, DOWN, buff=0.6)
        cta_group = VGroup(sub_button, cta_icons)

        self.play(FadeIn(cta_group, shift=UP), run_time=0.8)

        # Add cursor and simulate clicks
        cursor_poly = Polygon(
            ORIGIN, DOWN * 0.4 + RIGHT * 0.1, DOWN * 0.25 + RIGHT * 0.18, 
            DOWN * 0.35 + RIGHT * 0.32, DOWN * 0.3 + RIGHT * 0.35, 
            DOWN * 0.2 + RIGHT * 0.2, DOWN * 0.25 + RIGHT * 0.3,
            color=TEXT_COLOR, fill_color=TEXT_COLOR, fill_opacity=1
        ).scale(0.8)
        cursor = VGroup(cursor_poly).move_to(RIGHT * 4.5 + DOWN * 3)
        self.play(FadeIn(cursor), run_time=0.4)

        # 1. Click SUBSCRIBE
        self.play(cursor.animate.move_to(sub_btn_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(sub_button.animate.scale(0.92), cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02), run_time=0.15)
        new_sub_text = Text("SUBSCRIBED", font_size=24, color="#64748B", weight=BOLD, font="Arial")
        self.play(
            sub_btn_box.animate.scale(1.0/0.92).set_fill(color="#E2E8F0"),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Transform(sub_text, new_sub_text),
            yt_icon_box.animate.scale(1.0/0.92).set_fill(color="#CBD5E1"),
            yt_triangle.animate.scale(1.0/0.92).set_fill(color="#E2E8F0").set_stroke(color="#E2E8F0"),
            bell_body.animate.scale(1.0/0.92).set_fill(color="#64748B"),
            bell_base.animate.scale(1.0/0.92).set_fill(color="#64748B"),
            bell_clapper.animate.scale(1.0/0.92).set_fill(color="#64748B"),
            run_time=0.25
        )
        self.play(Rotate(bell_icon, angle=0.15, about_point=bell_icon.get_top(), rate_func=there_and_back), run_time=0.15)
        self.play(Rotate(bell_icon, angle=-0.15, about_point=bell_icon.get_top(), rate_func=there_and_back), run_time=0.15)

        # 2. Click LIKE
        self.play(cursor.animate.move_to(like_icon.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(like_icon.animate.scale(0.9), cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02), run_time=0.15)
        self.play(
            like_icon.animate.scale(1.0/0.9).set_color(BLUE),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(like_icon.get_center(), color=BLUE, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 3. Click COMMENT
        self.play(cursor.animate.move_to(comment_icon.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(comment_icon.animate.scale(0.9), cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02), run_time=0.15)
        self.play(
            comment_icon.animate.scale(1.0/0.9).set_color(AMBER),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(comment_icon.get_center(), color=AMBER, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 4. Click SHARE
        self.play(cursor.animate.move_to(share_icon.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(share_icon.animate.scale(0.9), cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02), run_time=0.15)
        self.play(
            share_icon.animate.scale(1.0/0.9).set_color(GREEN),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(share_icon.get_center(), color=GREEN, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # Retract cursor and end
        self.play(cursor.animate.move_to(RIGHT * 4.5 + DOWN * 3), FadeOut(cursor), run_time=0.4)
        self.wait(1.188)
