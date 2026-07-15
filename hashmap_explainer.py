from manim import *

class HashMapExplainer(Scene):
    def construct(self):
        # Palette configuration (White canvas, vibrant colorful elements)
        BG_COLOR = "#FFFFFF"
        BOX_BORDER = "#334155"       # dark slate, crisp on white
        BOX_FILL = "#F1F5F9"         # very light gray fill so boxes read on white
        HASH_COLOR = "#2563EB"       # vivid blue
        ALICE_COLOR = "#059669"      # vivid green
        BOB_COLOR = "#EA580C"        # vivid orange
        COLLISION_COLOR = "#DC2626"  # vivid red
        TEXT_COLOR = "#1E293B"       # near-black, readable on white
        HIGHLIGHT_COLOR = "#D97706"  # amber
        MUTED_TEXT = "#64748B"       # for secondary labels (index numbers, hints)

        self.camera.background_color = BG_COLOR

        # --- Caption Setup ---
        caption_box = RoundedRectangle(
            width=12, height=1.3, corner_radius=0.15,
            stroke_color=BOX_BORDER, stroke_width=1.5,
            fill_color="#F8FAFC", fill_opacity=0.95
        ).to_edge(DOWN, buff=0.4)

        caption_text = Paragraph(
            "Ever wonder how your phone finds a contact instantly,\neven with 10,000 saved? That's a hash map.",
            font_size=18, font="Sans", color=TEXT_COLOR, line_spacing=0.5
        ).move_to(caption_box.get_center())

        caption_group = VGroup(caption_box, caption_text)
        self.add(caption_group)

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
        # 1. THE HOOK (0:00 - 0:07)
        # =========================================================================

        # Phone mockup — keep the phone "screen" dark so it reads as a real device,
        # even while the canvas around it is white
        phone = RoundedRectangle(
            width=3.2, height=5.5, corner_radius=0.3,
            stroke_color=BOX_BORDER, stroke_width=3,
            fill_color="#0F172A", fill_opacity=0.95
        ).shift(UP * 0.5)

        phone_screen_title = Text("Contacts", font_size=18, color="#F1F5F9", weight=BOLD).next_to(phone.get_top(), DOWN, buff=0.3)

        search_bar = RoundedRectangle(
            width=2.6, height=0.4, corner_radius=0.08,
            stroke_color="#334155", stroke_width=1,
            fill_color="#1E293B", fill_opacity=1
        ).next_to(phone_screen_title, DOWN, buff=0.2)
        search_text = Text("Search...", font_size=10, color="#94A3B8").move_to(search_bar.get_center() + LEFT * 0.5)

        contact_names = ["Aaron", "Abby", "Alex", "Alice", "Ben", "Bob", "Charlie", "David"]
        contact_list = VGroup(*[
            VGroup(
                Text(name, font_size=14, color="#F1F5F9"),
                Line(start=LEFT*1.2, end=RIGHT*1.2, stroke_color="#334155", stroke_width=1)
            ).arrange(DOWN, buff=0.1)
            for name in contact_names
        ]).arrange(DOWN, buff=0.15).next_to(search_bar, DOWN, buff=0.3)

        phone_ui = VGroup(phone, phone_screen_title, search_bar, search_text, contact_list)
        self.play(FadeIn(phone_ui, shift=UP))
        self.wait(1.5)

        play_caption("That's a hash map. Let's break it down.", wait_time=5.1)

        # Transition phone to array grid
        array_boxes = VGroup(*[
            Square(side_length=0.8, stroke_color=BOX_BORDER, stroke_width=2, fill_color=BOX_FILL, fill_opacity=1)
            for _ in range(10)
        ]).arrange(RIGHT, buff=0.15).move_to(UP * 0.4)

        index_labels = VGroup(*[
            Text(str(i), font_size=14, color=MUTED_TEXT).next_to(array_boxes[i], DOWN, buff=0.12)
            for i in range(10)
        ])
        array_group = VGroup(array_boxes, index_labels)

        self.play(
            FadeOut(phone_ui, shift=DOWN),
            FadeIn(array_group, shift=UP)
        )
        self.wait(1.0)

        # =========================================================================
        # 2. THE CORE IDEA (0:07 - 0:20)
        # =========================================================================
        play_caption("A hash map stores data in key-value pairs.", wait_time=1.0)

        self.play(array_group.animate.shift(DOWN * 1.2))

        # Hash Function box
        hash_box = RoundedRectangle(
            width=2.8, height=1.4, corner_radius=0.2,
            stroke_color=HASH_COLOR, stroke_width=3,
            fill_color="#EFF6FF", fill_opacity=1
        ).shift(UP * 1.5)
        hash_label = Text("Hash Function", font_size=20, color=HASH_COLOR, weight=BOLD).move_to(hash_box.get_center() + UP * 0.15)
        hash_desc = Text("h(key) % size", font_size=10, color=MUTED_TEXT).next_to(hash_label, DOWN, buff=0.1)
        hash_machine = VGroup(hash_box, hash_label, hash_desc)

        self.play(FadeIn(hash_machine, shift=DOWN))
        self.wait(0.5)

        play_caption("Say you want to store 'Alice' with her phone number.", wait_time=1.5)

        alice_key = Text("Alice", font_size=18, color=ALICE_COLOR, weight=BOLD).next_to(hash_box, LEFT, buff=1.8)
        self.play(FadeIn(alice_key, shift=RIGHT))
        self.wait(0.5)

        play_caption("The hash map runs the key 'Alice' through a hash function —\na formula that turns it into a number.", wait_time=2.9)

        self.play(
            alice_key.animate.move_to(hash_box.get_center()).set_opacity(0),
            run_time=1.2
        )

        flash = Flash(hash_box.get_center(), color=HASH_COLOR, line_length=0.2, num_lines=8, flash_radius=0.4)
        self.play(flash)

        output_arrow = Arrow(start=hash_box.get_right(), end=hash_box.get_right() + RIGHT * 1.2, color=HASH_COLOR, buff=0.1)
        output_num = Text("7", font_size=32, color=ALICE_COLOR, weight=BOLD).next_to(output_arrow, RIGHT)
        self.play(Create(output_arrow), FadeIn(output_num, shift=RIGHT))
        self.wait(1.5)

        # =========================================================================
        # 3. STORING THE DATA (0:20 - 0:35)
        # =========================================================================
        play_caption("That number becomes the index — the exact slot\nin an array where the value gets stored.", wait_time=3.0)

        target_slot = array_boxes[7]
        self.play(
            output_num.animate.move_to(target_slot.get_center()).set_opacity(0),
            output_arrow.animate.set_opacity(0),
            run_time=1.2
        )

        alice_card = RoundedRectangle(
            width=0.74, height=0.74, corner_radius=0.08,
            stroke_color=ALICE_COLOR, stroke_width=2,
            fill_color=ALICE_COLOR, fill_opacity=0.15
        ).move_to(target_slot.get_center())

        alice_text = Text("Alice", font_size=10, color=ALICE_COLOR, weight=BOLD).move_to(target_slot.get_center())
        alice_stored = VGroup(alice_card, alice_text)

        self.play(
            target_slot.animate.set_stroke(color=ALICE_COLOR, width=3),
            FadeIn(alice_stored, scale=0.8),
            Flash(target_slot.get_center(), color=ALICE_COLOR, line_length=0.15, flash_radius=0.45)
        )
        self.wait(1.5)

        play_caption("So next time you look up 'Alice', the hash map runs the same formula,\ngets the same number...", wait_time=3.2)

        glass_circle = Circle(radius=0.18, color=HIGHLIGHT_COLOR, stroke_width=3)
        glass_handle = Line(
            start=glass_circle.get_bottom() + LEFT * 0.05,
            end=glass_circle.get_bottom() + DOWN * 0.18 + LEFT * 0.18,
            color=HIGHLIGHT_COLOR, stroke_width=3
        )
        magnifying_glass = VGroup(glass_circle, glass_handle).move_to(array_boxes[0].get_center() + UP * 0.8)

        self.play(FadeIn(magnifying_glass))
        self.wait(0.5)

        play_caption("...and jumps straight to that slot. No searching required.\nThat's why it's so fast — O(1) on average.", wait_time=4.7)

        self.play(magnifying_glass.animate.move_to(target_slot.get_center() + UP * 0.8), run_time=1.0)
        self.play(
            target_slot.animate.scale(1.15),
            alice_stored.animate.scale(1.15),
            rate_func=there_and_back,
            run_time=0.8
        )
        self.play(FadeOut(magnifying_glass))
        self.wait(1.0)

        # =========================================================================
        # 4. THE COLLISION PROBLEM (0:35 - 0:55)
        # =========================================================================
        play_caption("But here's the catch: two different keys can hash to the same index.", wait_time=0.5)

        self.play(target_slot.animate.set_stroke(color=ALICE_COLOR, width=2))

        bob_key = Text("Bob", font_size=18, color=BOB_COLOR, weight=BOLD).next_to(hash_box, LEFT, buff=1.8)
        self.play(FadeIn(bob_key, shift=RIGHT))
        self.wait(0.8)

        play_caption("Say 'Bob' also hashes to slot 7.", wait_time=0.5)

        self.play(bob_key.animate.move_to(hash_box.get_center()).set_opacity(0), run_time=1.2)
        flash_bob = Flash(hash_box.get_center(), color=HASH_COLOR, line_length=0.2, num_lines=8, flash_radius=0.4)

        bob_arrow = Arrow(start=hash_box.get_right(), end=hash_box.get_right() + RIGHT * 1.2, color=HASH_COLOR, buff=0.1)
        bob_output = Text("7", font_size=32, color=BOB_COLOR, weight=BOLD).next_to(bob_arrow, RIGHT)

        self.play(
            flash_bob,
            Create(bob_arrow),
            FadeIn(bob_output, shift=RIGHT)
        )
        self.wait(1.2)

        play_caption("The hash map can't just overwrite Alice's data —\nso it needs a backup plan.", wait_time=0.6)

        self.play(
            bob_output.animate.move_to(target_slot.get_center()).set_opacity(0),
            bob_arrow.animate.set_opacity(0),
            run_time=1.2
        )

        collision_warning = Text("COLLISION!", font_size=18, color=COLLISION_COLOR, weight=BOLD).next_to(target_slot, UP, buff=0.4)
        collision_flash = Flash(target_slot.get_center(), color=COLLISION_COLOR, line_length=0.25, num_lines=12, flash_radius=0.5)

        self.play(
            target_slot.animate.set_stroke(color=COLLISION_COLOR, width=4.0),
            FadeIn(collision_warning, shift=UP),
            collision_flash
        )
        self.wait(1.5)
        self.play(FadeOut(collision_warning))

        # =========================================================================
        # 5. HOW COLLISIONS ARE HANDLED (0:55 - 1:10)
        # =========================================================================
        play_caption("The most common fix: each slot holds a small linked list.", wait_time=0.8)

        self.play(
            FadeOut(hash_machine),
            FadeOut(index_labels),
            *[array_boxes[i].animate.set_opacity(0.15) for i in range(10) if i != 7]
        )

        self.play(
            target_slot.animate.move_to(ORIGIN + LEFT * 3).scale(1.5).set_stroke(color=HASH_COLOR, width=3)
        )

        self.play(
            alice_stored.animate.move_to(target_slot.get_center()).scale(1.3)
        )
        self.wait(0.5)

        play_caption("If two keys collide, they just chain together in that same slot.", wait_time=0.8)

        alice_node_box = Rectangle(width=1.6, height=0.9, stroke_color=ALICE_COLOR, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1)
        alice_node_box.move_to(LEFT * 2.5 + UP * 0.5)
        alice_node_label = Text("Alice", font_size=14, color=TEXT_COLOR, weight=BOLD).move_to(alice_node_box.get_center() + LEFT * 0.3)
        alice_node_pointer = Line(start=alice_node_box.get_center() + RIGHT * 0.2 + UP * 0.45, end=alice_node_box.get_center() + RIGHT * 0.2 + DOWN * 0.45, stroke_color=BOX_BORDER, stroke_width=1.5)
        alice_node = VGroup(alice_node_box, alice_node_label, alice_node_pointer)

        bob_node_box = Rectangle(width=1.6, height=0.9, stroke_color=BOB_COLOR, stroke_width=2.5, fill_color=BOX_FILL, fill_opacity=1)
        bob_node_box.move_to(RIGHT * 1.5 + UP * 0.5)
        bob_node_label = Text("Bob", font_size=14, color=TEXT_COLOR, weight=BOLD).move_to(bob_node_box.get_center() + LEFT * 0.3)
        bob_node_pointer = Line(start=bob_node_box.get_center() + RIGHT * 0.2 + UP * 0.45, end=bob_node_box.get_center() + RIGHT * 0.2 + DOWN * 0.45, stroke_color=BOX_BORDER, stroke_width=1.5)
        bob_node = VGroup(bob_node_box, bob_node_label, bob_node_pointer)

        node_arrow = Arrow(start=alice_node_box.get_right() - RIGHT * 0.2, end=bob_node_box.get_left(), color=HIGHLIGHT_COLOR, stroke_width=3, buff=0.1)

        play_caption("So slot 7 now holds both Alice and Bob...", wait_time=0.8)

        self.play(
            FadeOut(target_slot),
            ReplacementTransform(alice_stored, alice_node),
            FadeIn(bob_node, shift=RIGHT),
            Create(node_arrow)
        )
        self.wait(1.0)

        play_caption("...and the hash map checks each one until it finds the right key.", wait_time=0.8)

        lookup_pointer = Arrow(start=alice_node_box.get_top() + UP * 0.8, end=alice_node_box.get_top(), color=HIGHLIGHT_COLOR, stroke_width=4)
        lookup_label = Text("Find 'Bob'", font_size=12, color=HIGHLIGHT_COLOR, weight=BOLD).next_to(lookup_pointer, UP, buff=0.1)
        lookup_group = VGroup(lookup_pointer, lookup_label)

        self.play(FadeIn(lookup_group))
        self.wait(0.8)

        self.play(
            alice_node_box.animate.set_stroke(color=COLLISION_COLOR, width=4),
            run_time=0.6
        )
        self.wait(0.6)

        self.play(
            lookup_group.animate.shift(RIGHT * 4.0),
            run_time=1.0
        )

        self.play(
            bob_node_box.animate.set_stroke(color=ALICE_COLOR, width=4),
            Flash(bob_node_box.get_center(), color=ALICE_COLOR, line_length=0.2, num_lines=8, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(1.5)

        self.play(
            FadeOut(lookup_group),
            FadeOut(alice_node),
            FadeOut(bob_node),
            FadeOut(node_arrow)
        )

        # =========================================================================
        # 6. CLOSER (1:10 - 1:15)
        # =========================================================================
        play_caption("That's a hash map — instant lookups, one clever formula...", wait_time=0.5)

        array_boxes.set_opacity(1.0)
        target_slot.scale(1.0/1.5).move_to(array_boxes[7].get_center()).set_stroke(color=BOX_BORDER, width=2)

        chain_indicator = VGroup(
            RoundedRectangle(width=0.3, height=0.6, corner_radius=0.04, stroke_color=ALICE_COLOR, fill_color=ALICE_COLOR, fill_opacity=0.25),
            RoundedRectangle(width=0.3, height=0.6, corner_radius=0.04, stroke_color=BOB_COLOR, fill_color=BOB_COLOR, fill_opacity=0.25)
        ).arrange(RIGHT, buff=0.06).move_to(target_slot.get_center())

        self.play(
            FadeIn(target_slot),
            FadeIn(chain_indicator),
            FadeIn(index_labels)
        )
        self.wait(1.5)

        play_caption("...and a backup plan for when two keys land in the same spot.", wait_time=0.6)

        final_title = Text("Hash Maps, Explained.", font_size=36, color=HASH_COLOR, weight=BOLD).move_to(UP * 0.5)
        final_subtitle = Text("O(1) Lookups • Collision Chaining", font_size=18, color=TEXT_COLOR).next_to(final_title, DOWN, buff=0.3)
        final_card = VGroup(final_title, final_subtitle)

        self.play(
            FadeOut(array_group),
            FadeOut(target_slot),
            FadeOut(chain_indicator),
            FadeIn(final_card, scale=0.8)
        )
        self.wait(3.0)

        # =========================================================================
        # 7. CALL TO ACTION (CTA)
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
            stroke_color=COLLISION_COLOR, stroke_width=2,
            fill_color=COLLISION_COLOR, fill_opacity=1
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
        # Shift to start position
        cursor = VGroup(cursor_poly).move_to(RIGHT * 4.5 + DOWN * 3)
        self.play(FadeIn(cursor), run_time=0.4)

        # 1. Animate clicking LIKE
        self.play(cursor.animate.move_to(like_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        # Press down
        self.play(
            like_box.animate.scale(0.92), 
            like_label.animate.scale(0.92),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        # Release and activate
        self.play(
            like_box.animate.scale(1.0/0.92).set_fill(color=HASH_COLOR).set_stroke(color=HASH_COLOR),
            like_label.animate.scale(1.0/0.92).set_color(color=WHITE),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(like_box.get_center(), color=HASH_COLOR, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 2. Animate clicking SUBSCRIBE
        self.play(cursor.animate.move_to(sub_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        # Press down
        self.play(
            sub_box.animate.scale(0.92),
            sub_label.animate.scale(0.92),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        # Release and Subscribed
        new_sub_label = Text("Subscribed", font_size=12, color="#475569", weight=BOLD).move_to(sub_box.get_center())
        self.play(
            sub_box.animate.scale(1.0/0.92).set_fill(color="#E2E8F0").set_stroke(color="#CBD5E1"),
            ReplacementTransform(sub_label, new_sub_label),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(sub_box.get_center(), color=COLLISION_COLOR, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 3. Animate clicking SHARE
        self.play(cursor.animate.move_to(share_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        # Press down
        self.play(
            share_box.animate.scale(0.92),
            share_label.animate.scale(0.92),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        # Release and activate
        self.play(
            share_box.animate.scale(1.0/0.92).set_fill(color=ALICE_COLOR).set_stroke(color=ALICE_COLOR),
            share_label.animate.scale(1.0/0.92).set_color(color=WHITE),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(share_box.get_center(), color=ALICE_COLOR, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # Retract cursor and end
        self.play(
            cursor.animate.move_to(RIGHT * 4.5 + DOWN * 3),
            FadeOut(cursor),
            run_time=0.4
        )
        self.wait(0.3)
