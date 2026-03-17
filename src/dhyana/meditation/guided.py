"""Guided meditation sessions with scripts."""

import random
from typing import Optional

from dhyana.models import GuidedScript, MeditationStyle, Difficulty


# 22 guided meditation scripts
GUIDED_SCRIPTS: list[GuidedScript] = [
    # BREATH AWARENESS (3 scripts)
    GuidedScript(
        id="breath_01",
        title="Arriving in the Present Moment",
        style=MeditationStyle.BREATH_AWARENESS,
        duration_minutes=10,
        introduction=(
            "Welcome. Find a comfortable seat and gently close your eyes. "
            "Allow your shoulders to drop, your jaw to soften. "
            "There is nowhere you need to be right now other than here. "
            "Let this be a homecoming to the present moment."
        ),
        body_segments=[
            "Bring your attention to your breath. Do not try to change it. "
            "Simply notice the air flowing in through your nostrils, cool on the inhale, "
            "warm on the exhale. Let each breath be exactly as it is.",

            "Now notice the rhythm. The rise and fall of your chest. The gentle expansion "
            "of your belly. Each breath is a wave arriving on shore and retreating. "
            "You are the shore. Steady, present, unchanged.",

            "Your mind will wander. This is not a problem. It is what minds do. "
            "When you notice you have drifted, gently return. No judgment. "
            "Each return is a moment of awakening, a small victory of awareness.",

            "Deepen your attention now. Feel the brief pause between the inhale and the exhale. "
            "In that gap, there is stillness. Rest there for a moment. "
            "Then let the breath carry you onward, effortlessly.",
        ],
        closing=(
            "Gently begin to widen your awareness. Feel the space around you. "
            "Notice the sounds of the room. Wiggle your fingers and toes. "
            "When you are ready, slowly open your eyes. "
            "Carry this sense of presence with you into whatever comes next."
        ),
        focus_areas=["breath", "presence", "relaxation"],
    ),
    GuidedScript(
        id="breath_02",
        title="Counting Breaths for Focus",
        style=MeditationStyle.BREATH_AWARENESS,
        duration_minutes=10,
        introduction=(
            "Settle into your seat. Let your body find its natural alignment. "
            "This practice uses counting as a gentle scaffold for your attention. "
            "There is no right or wrong here. Just breath and number."
        ),
        body_segments=[
            "Breathe naturally. On each exhale, count silently. "
            "Inhale... exhale, one. Inhale... exhale, two. "
            "Continue up to ten, then begin again at one.",

            "If you lose count or go past ten, simply start again. "
            "The counting is not a goal. It is a thread that keeps you "
            "connected to the present breath. Nothing more.",

            "Notice how the mind settles when given this gentle task. "
            "The gap between thoughts may widen. The breath may slow. "
            "Allow this natural deepening without forcing it.",

            "Now release the counting. Simply rest in the flow of breathing. "
            "Feel the ease that comes from a settled mind. "
            "You have arrived nowhere new. You have simply stopped leaving.",
        ],
        closing=(
            "Take a slightly deeper breath. Feel gratitude for these minutes "
            "of quiet attention. Open your eyes when you feel ready."
        ),
        focus_areas=["concentration", "breath", "focus"],
    ),
    GuidedScript(
        id="breath_03",
        title="4-7-8 Calming Breath",
        style=MeditationStyle.BREATH_AWARENESS,
        duration_minutes=8,
        introduction=(
            "This practice uses a specific breathing pattern to activate "
            "your parasympathetic nervous system, the part of you that knows "
            "how to rest. It is simple and profoundly calming."
        ),
        body_segments=[
            "Breathe in through your nose for a count of four. "
            "One... two... three... four. Let your lungs fill gently.",

            "Now hold the breath for seven counts. "
            "One... two... three... four... five... six... seven. "
            "Not straining. Simply pausing.",

            "Exhale slowly through your mouth for eight counts. "
            "One... two... three... four... five... six... seven... eight. "
            "Let everything release.",

            "Repeat this cycle three more times. With each round, "
            "feel your body softening, your nervous system settling. "
            "Like a lake becoming still after wind.",
        ],
        closing=(
            "Return to natural breathing. Notice how different you feel. "
            "Your body knows how to rest. You have simply reminded it."
        ),
        focus_areas=["calming", "stress relief", "breathing technique"],
    ),

    # BODY SCAN (3 scripts)
    GuidedScript(
        id="body_01",
        title="Full Body Relaxation Scan",
        style=MeditationStyle.BODY_SCAN,
        duration_minutes=15,
        introduction=(
            "Lie down or sit comfortably. This practice will guide your attention "
            "through your entire body. There is nothing to fix or change. "
            "Simply notice what is present with kind curiosity."
        ),
        body_segments=[
            "Bring awareness to the soles of your feet. Notice warmth, coolness, "
            "tingling, or nothing at all. Whatever is there is fine. "
            "Breathe softly and let the feet relax completely.",

            "Move your attention up through your ankles, calves, and knees. "
            "Feel the weight of your legs against the surface beneath you. "
            "With each exhale, let them grow heavier, more supported.",

            "Bring awareness to your hips and lower back. This area often holds "
            "tension we do not consciously recognize. Breathe into this space. "
            "Imagine the breath creating room, softness, release.",

            "Move through your abdomen and chest. Feel the gentle movement of breathing. "
            "Notice the heartbeat. This body has been carrying you faithfully. "
            "Offer it a moment of appreciation.",

            "Scan your hands, arms, and shoulders. Let the shoulders drop away "
            "from the ears. Feel the arms grow heavy and warm.",

            "Finally, bring attention to the neck, jaw, face, and scalp. "
            "Soften the muscles around the eyes. Unclench the jaw. "
            "Let the forehead smooth. Rest in whole-body awareness.",
        ],
        closing=(
            "Take a full, deep breath. Feel your entire body as one field of awareness. "
            "When you are ready, gently begin to move, stretching naturally. "
            "Open your eyes with softness."
        ),
        focus_areas=["relaxation", "body awareness", "tension release"],
    ),
    GuidedScript(
        id="body_02",
        title="Tension and Release Body Scan",
        style=MeditationStyle.BODY_SCAN,
        duration_minutes=12,
        introduction=(
            "This practice combines progressive muscle relaxation with mindful scanning. "
            "You will gently tense and then release each area to deepen relaxation."
        ),
        body_segments=[
            "Start with your feet. Curl your toes tightly for five seconds. "
            "Then release. Feel the difference between tension and relaxation. "
            "This is the contrast your body can teach you.",

            "Move to your legs. Tense your calves and thighs. Hold... and release. "
            "Notice the warm wave of relaxation flowing through your legs.",

            "Clench your fists. Tighten your forearms. Hold... and release. "
            "Feel your hands open like flowers blooming.",

            "Shrug your shoulders up toward your ears. Hold that tension. "
            "Now let go completely. Feel the shoulders melt downward.",

            "Scrunch your face tightly. Squeeze your eyes shut. Hold... and release. "
            "Let your face become smooth, open, relaxed.",
        ],
        closing=(
            "Lie still for a moment in total relaxation. Your body has released "
            "what it was holding. Carry this lightness forward."
        ),
        focus_areas=["progressive relaxation", "tension release", "body awareness"],
    ),
    GuidedScript(
        id="body_03",
        title="Healing Light Body Scan",
        style=MeditationStyle.BODY_SCAN,
        duration_minutes=15,
        introduction=(
            "Imagine a warm, golden light above your head. "
            "As we scan the body, this light will move through each area, "
            "bringing warmth, healing, and deep relaxation."
        ),
        body_segments=[
            "The golden light descends to the crown of your head. "
            "Feel it melting into your scalp, releasing any tightness. "
            "It flows across your forehead, softening every line.",

            "The light moves through your face, warming your cheeks, "
            "relaxing your jaw. It flows down your neck, dissolving tension "
            "like sunlight dissolving morning frost.",

            "It fills your chest with warmth. Your heart bathes in golden light. "
            "It moves through your arms to your fingertips, "
            "each cell receiving warmth and care.",

            "The light continues through your abdomen, lower back, and hips. "
            "Wherever it touches, tension dissolves. "
            "Your entire core is glowing with gentle warmth.",

            "Finally, the light flows through your legs to the soles of your feet. "
            "Your whole body is now filled with this healing radiance. "
            "Rest here. You are whole.",
        ],
        closing=(
            "The light remains within you, a gentle warmth you can return to anytime. "
            "Slowly bring movement back into your body and open your eyes."
        ),
        focus_areas=["healing", "visualization", "relaxation"],
    ),

    # LOVING-KINDNESS (3 scripts)
    GuidedScript(
        id="lk_01",
        title="Heart of Compassion",
        style=MeditationStyle.LOVING_KINDNESS,
        duration_minutes=15,
        introduction=(
            "This practice cultivates the boundless quality of loving-kindness. "
            "We begin by turning warmth toward ourselves and gradually expand "
            "outward until our compassion has no borders."
        ),
        body_segments=[
            "Place your hand over your heart. Feel its steady rhythm. "
            "This heart has been beating for you every moment of your life. "
            "Silently say: May I be happy. May I be healthy. May I be safe. "
            "May I live with ease.",

            "Bring to mind someone you love deeply. See their face. "
            "Feel the natural warmth that arises. Direct these wishes to them: "
            "May you be happy. May you be healthy. May you be safe. "
            "May you live with ease.",

            "Now think of someone neutral: a neighbor, a cashier, someone you see "
            "but do not really know. They too have hopes, fears, and dreams. "
            "May you be happy. May you be healthy. May you be safe. "
            "May you live with ease.",

            "With courage, bring to mind someone you find difficult. "
            "This does not mean approving of harmful actions. "
            "It means recognizing shared humanity. "
            "May you be happy. May you be healthy. May you be safe.",

            "Finally, expand your awareness to include all beings everywhere. "
            "North, south, east, west. Near and far. Known and unknown. "
            "May all beings be happy. May all beings be free from suffering.",
        ],
        closing=(
            "Rest in this vast, warm awareness. The capacity for loving-kindness "
            "is already within you. You have simply uncovered it. "
            "Open your eyes and carry this warmth into the world."
        ),
        focus_areas=["compassion", "loving-kindness", "self-love"],
    ),
    GuidedScript(
        id="lk_02",
        title="Self-Compassion Practice",
        style=MeditationStyle.LOVING_KINDNESS,
        duration_minutes=12,
        introduction=(
            "Today we focus entirely on directing loving-kindness toward yourself. "
            "This is not selfish. It is necessary. You cannot pour from an empty cup."
        ),
        body_segments=[
            "Think of yourself as you were as a small child. Innocent, open, deserving of love. "
            "That child is still within you. Speak to them now: "
            "You are enough. You are worthy of love, exactly as you are.",

            "Think of a struggle you are currently facing. "
            "Instead of judging yourself, offer the compassion you would give a dear friend. "
            "May I be gentle with myself. May I accept my imperfections.",

            "Place both hands on your heart. Feel the warmth. "
            "Repeat slowly: I forgive myself for the times I have fallen short. "
            "I am doing the best I can. And that is enough.",

            "Imagine yourself surrounded by a circle of people who love you, "
            "past and present. Feel their support. You are not alone. "
            "You are held in a web of care that extends further than you know.",
        ],
        closing=(
            "Carry this self-compassion with you. When the inner critic speaks, "
            "remember this warmth. You deserve the same kindness you give to others."
        ),
        focus_areas=["self-compassion", "self-love", "healing"],
    ),
    GuidedScript(
        id="lk_03",
        title="Radiating Kindness to the World",
        style=MeditationStyle.LOVING_KINDNESS,
        duration_minutes=10,
        introduction=(
            "In this practice, we will visualize kindness as a light that radiates "
            "from your heart outward in ever-widening circles."
        ),
        body_segments=[
            "Begin by sensing a warm glow in the center of your chest. "
            "With each breath, it grows brighter. This is your innate capacity for love.",

            "Let the light expand to fill the room. Everyone in this space "
            "is bathed in warmth. May all in this room be at peace.",

            "The light extends beyond the walls, across your neighborhood, your city. "
            "Millions of people, each with their own joys and sorrows. "
            "May all beings in this city be happy.",

            "Now let the light extend across the entire planet. "
            "Every continent, every ocean, every creature. "
            "May all beings everywhere be free from suffering. "
            "May all beings find peace.",
        ],
        closing=(
            "The light remains, glowing steadily in your heart. "
            "You can return to it whenever you need to. Open your eyes."
        ),
        focus_areas=["compassion", "visualization", "universal love"],
    ),

    # VISUALIZATION (3 scripts)
    GuidedScript(
        id="vis_01",
        title="Mountain Meditation",
        style=MeditationStyle.VISUALIZATION,
        duration_minutes=12,
        introduction=(
            "In this practice, you will embody the qualities of a mountain: "
            "stability, strength, and unshakable presence through all seasons."
        ),
        body_segments=[
            "Visualize a beautiful mountain. See its broad base rooted in the earth. "
            "Its peak reaching into the sky. It has stood for millennia, "
            "weathering every storm.",

            "Now imagine that you are this mountain. Your base is your sitting position, "
            "grounded and stable. Your spine is the mountain's core, strong and upright. "
            "Your head is the peak, touching the open sky.",

            "Seasons pass over you. Spring brings fresh growth. Summer brings warm sun. "
            "Autumn brings change and letting go. Winter brings stillness and rest. "
            "Through it all, the mountain remains. You remain.",

            "Storms come: clouds, wind, rain, even lightning. "
            "But the mountain does not move. It does not resist. It simply is. "
            "You can be this mountain in your life. Present through every season.",
        ],
        closing=(
            "As you open your eyes, carry the mountain within you. "
            "Its strength is your strength. Its stillness is available to you always."
        ),
        focus_areas=["stability", "grounding", "resilience"],
    ),
    GuidedScript(
        id="vis_02",
        title="Safe Place Sanctuary",
        style=MeditationStyle.VISUALIZATION,
        duration_minutes=10,
        introduction=(
            "You are about to create a personal sanctuary in your mind. "
            "A place of absolute safety and peace that you can visit anytime."
        ),
        body_segments=[
            "Imagine a door appearing before you. It can look however you like. "
            "Behind this door is your sanctuary. Take a breath and step through.",

            "You find yourself in a place of natural beauty. "
            "It might be a forest clearing, a beach, a mountain meadow, or a cozy room. "
            "Let the image form naturally. Trust what appears.",

            "Engage your senses. What colors do you see? What sounds surround you? "
            "What does the air feel like on your skin? Is there a scent? "
            "Make this place vivid and real.",

            "Find a comfortable place to rest in your sanctuary. "
            "Nothing can disturb you here. No demands, no worries, no judgments. "
            "You are completely safe. Breathe deeply and rest.",
        ],
        closing=(
            "Know that this sanctuary is always available to you. "
            "You can return here anytime by closing your eyes and stepping through the door. "
            "Gently return to the room and open your eyes."
        ),
        focus_areas=["safety", "relaxation", "anxiety relief"],
    ),
    GuidedScript(
        id="vis_03",
        title="River of Thoughts",
        style=MeditationStyle.VISUALIZATION,
        duration_minutes=10,
        introduction=(
            "In this meditation, you will learn to observe your thoughts "
            "without being carried away by them, using the metaphor of a river."
        ),
        body_segments=[
            "Imagine you are sitting on the bank of a gently flowing river. "
            "The water is clear. The sun is warm. You are comfortable and safe.",

            "Each thought that arises in your mind becomes a leaf floating on the water. "
            "Watch each thought-leaf appear, float past you, and disappear downstream. "
            "You do not need to grab any of them.",

            "Some leaves are beautiful. Some are wilted. Some carry pleasant memories, "
            "others carry worries. Let them all float by equally. "
            "You are not the leaves. You are the one watching from the bank.",

            "If you find yourself in the river, swept up in a thought, "
            "simply notice, climb back on the bank, and resume watching. "
            "This is the practice. This gentle returning.",
        ],
        closing=(
            "The river continues flowing. The thoughts continue arising. "
            "But you have discovered something: you can choose to watch "
            "rather than be swept away. Open your eyes."
        ),
        focus_areas=["mindfulness", "detachment", "thought observation"],
    ),

    # MANTRA (2 scripts)
    GuidedScript(
        id="mantra_01",
        title="Om Meditation",
        style=MeditationStyle.MANTRA,
        duration_minutes=15,
        introduction=(
            "Om is considered the primordial sound, the vibration from which "
            "all creation emerges. In this practice, we will use this sacred syllable "
            "to settle the mind and connect with something vast."
        ),
        body_segments=[
            "Take three deep breaths to settle. On your next exhale, "
            "let the sound 'Om' emerge naturally from your chest. "
            "Aaa... Ooo... Mmm. Feel the vibration in your body.",

            "Continue chanting Om, either aloud or silently. "
            "Feel 'Aaa' vibrating in your belly, 'Ooo' in your chest, "
            "and 'Mmm' in your head. The whole body becomes an instrument.",

            "After several rounds, let the chanting become silent. "
            "Repeat Om only in your mind. Notice how the inner vibration continues. "
            "The silence after Om is as important as the sound itself.",

            "Rest in the silence. The mantra has settled your mind like a stone "
            "settling to the bottom of a clear lake. Be still here.",
        ],
        closing=(
            "Bring your palms together at your heart. Bow gently inward. "
            "The sound of Om continues within you, always. "
            "Open your eyes when you are ready."
        ),
        focus_areas=["mantra", "vibration", "deep meditation"],
    ),
    GuidedScript(
        id="mantra_02",
        title="So Hum - I Am That",
        style=MeditationStyle.MANTRA,
        duration_minutes=15,
        introduction=(
            "So Hum is a natural mantra. It is the sound the breath makes: "
            "'So' on the inhale, 'Hum' on the exhale. It means 'I am That,' "
            "connecting your individual self to the universal."
        ),
        body_segments=[
            "Breathe naturally. On the inhale, silently say 'So.' "
            "On the exhale, silently say 'Hum.' "
            "Let the mantra ride on the breath like a boat on gentle waves.",

            "So... I am. Hum... That. With each cycle, you affirm your connection "
            "to all that is. You are not separate. You are part of the whole.",

            "Let the mantra become softer, subtler. Eventually it may fade entirely, "
            "leaving only the breath and awareness. This is the goal: "
            "to be carried beyond the mantra into silence.",

            "Rest in whatever arises. Silence, stillness, spaciousness. "
            "If the mind becomes active, gently return to So Hum. "
            "The mantra is always there, patient and steady.",
        ],
        closing=(
            "Take a deep breath. Let the mantra go. Sit quietly for a moment, "
            "feeling the peace that has settled within you. Open your eyes."
        ),
        focus_areas=["mantra", "breath synchronization", "self-inquiry"],
    ),

    # VIPASSANA (2 scripts)
    GuidedScript(
        id="vip_01",
        title="Observing Impermanence",
        style=MeditationStyle.VIPASSANA,
        duration_minutes=20,
        introduction=(
            "Vipassana means seeing things as they truly are. In this practice, "
            "we observe body sensations with equanimity, understanding that "
            "everything that arises will also pass away."
        ),
        body_segments=[
            "Settle your attention on the area below the nostrils, above the upper lip. "
            "This small triangle of skin is your field of observation. "
            "What do you feel? Warmth? Coolness? Tingling? Nothing? "
            "Whatever it is, simply observe.",

            "Now begin a systematic scan from the top of your head. "
            "Move attention slowly, like a searchlight. Crown... forehead... "
            "temples... eyes... cheeks... nose... mouth... chin.",

            "Continue down through the neck, shoulders, arms, hands. "
            "Back, chest, abdomen, hips. Legs, knees, calves, feet. "
            "Wherever you find sensation, observe it. Pleasant or unpleasant, "
            "it will change. This is anicca: impermanence.",

            "Scan back upward now. Notice how sensations have already changed. "
            "What was strong may be subtle. What was absent may have appeared. "
            "Nothing stays the same. This is the deepest truth.",

            "Rest in equanimity. Do not crave pleasant sensations. "
            "Do not resist unpleasant ones. They are all equally impermanent. "
            "You are learning the art of non-reactivity.",
        ],
        closing=(
            "May the merit of this practice be shared with all beings. "
            "May all beings be happy. May all beings be liberated. "
            "Open your eyes slowly. Bhavatu sabba mangalam."
        ),
        focus_areas=["insight", "equanimity", "impermanence"],
        difficulty=Difficulty.INTERMEDIATE,
    ),
    GuidedScript(
        id="vip_02",
        title="Mindfulness of Breath and Body",
        style=MeditationStyle.VIPASSANA,
        duration_minutes=15,
        introduction=(
            "This practice follows the Anapanasati Sutta, mindfulness of breathing. "
            "We use the breath as a foundation and expand awareness to the whole body."
        ),
        body_segments=[
            "Begin with awareness of breathing. Simply know: breathing in, I know I am breathing in. "
            "Breathing out, I know I am breathing out.",

            "Breathing in, I am aware of my whole body. "
            "Breathing out, I calm my whole body. "
            "Let the breath soothe every cell.",

            "Now observe whatever sensation is most prominent. "
            "It might be the heartbeat, a tension, or a subtle vibration. "
            "Stay with it. Watch it change.",

            "Thoughts will arise. Note them as 'thinking' and return to the body. "
            "The body is always in the present moment. "
            "The mind often is not. Use the body to anchor yourself here.",
        ],
        closing=(
            "Gently widen your awareness. Feel the body as a whole. "
            "Take a deep breath and open your eyes with gratitude."
        ),
        focus_areas=["breath", "body awareness", "mindfulness"],
    ),

    # YOGA NIDRA (2 scripts)
    GuidedScript(
        id="yn_01",
        title="Deep Rest Yoga Nidra",
        style=MeditationStyle.YOGA_NIDRA,
        duration_minutes=25,
        introduction=(
            "Lie on your back in shavasana. Cover yourself with a blanket if you wish. "
            "Yoga Nidra is the sleep of the yogis: you will rest deeply while remaining aware. "
            "There is nothing to do. Simply follow the voice and allow yourself to be guided."
        ),
        body_segments=[
            "Set your sankalpa, your heartfelt resolve. A short, positive statement in present tense. "
            "For example: 'I am at peace.' Repeat it three times with full feeling. "
            "Plant it like a seed in the fertile soil of deep awareness.",

            "Rotation of consciousness. Bring awareness to each body part as it is named. "
            "Right thumb, index finger, middle finger, ring finger, little finger. "
            "Palm, back of hand, wrist, forearm, elbow, upper arm, shoulder. "
            "Right side of chest, right side of waist, right hip. "
            "Right thigh, knee, calf, ankle, heel, sole, top of foot, each toe.",

            "Now the left side. Left thumb, index finger, middle finger, ring finger, little finger. "
            "Palm, back of hand, wrist, forearm, elbow, upper arm, shoulder. "
            "Left side of chest, left side of waist, left hip. "
            "Left thigh, knee, calf, ankle, heel, sole, top of foot, each toe.",

            "Now the back of the body. Right shoulder blade, left shoulder blade. "
            "The whole back. The spine. The buttocks. The backs of the thighs. "
            "The calves. The heels.",

            "Experience pairs of opposites. Feel heaviness in the whole body... "
            "now lightness. Feel warmth spreading through the body... "
            "now coolness. Feel pain... now pleasure. Sorrow... now joy.",

            "Visualization: Imagine a clear blue sky. Vast, open, limitless. "
            "You are that sky. Thoughts and sensations are clouds passing through. "
            "Rest as the sky itself. Boundless awareness.",
        ],
        closing=(
            "Return to your sankalpa. Repeat it three times with conviction. "
            "Begin to deepen your breath. Feel the surface beneath you. "
            "Wiggle your fingers and toes. Roll to your right side. "
            "When you are ready, slowly sit up. The practice is complete."
        ),
        focus_areas=["deep rest", "relaxation", "subconscious healing"],
    ),
    GuidedScript(
        id="yn_02",
        title="Sleep Preparation Nidra",
        style=MeditationStyle.YOGA_NIDRA,
        duration_minutes=20,
        introduction=(
            "This practice is designed to be done in bed before sleep. "
            "If you fall asleep during the practice, that is perfectly fine. "
            "The instructions will continue to work on a subconscious level."
        ),
        body_segments=[
            "Feel the weight of your body sinking into the mattress. "
            "With each exhale, you become heavier. "
            "The bed is supporting you completely. You can let go.",

            "Bring awareness to your face. Soften the forehead. "
            "Let the eyebrows drift apart. Relax the tiny muscles around the eyes. "
            "Let the cheeks feel heavy. Unclench the jaw. Let the tongue rest.",

            "Feel a warm wave of relaxation flowing down from your head "
            "through your neck, shoulders, and arms. Down through your torso, "
            "hips, legs, and out through the soles of your feet.",

            "You are floating now. Between waking and sleeping. "
            "In this liminal space, the body heals, the mind releases, "
            "and deep rest unfolds. There is nothing to do. "
            "Simply rest. Rest. Rest.",
        ],
        closing=(
            "If you are still awake, allow yourself to drift into natural sleep. "
            "If you wish to remain awake, take a deep breath and sit up slowly."
        ),
        focus_areas=["sleep", "relaxation", "insomnia relief"],
    ),

    # ZAZEN (2 scripts)
    GuidedScript(
        id="zazen_01",
        title="Just Sitting (Shikantaza)",
        style=MeditationStyle.ZAZEN,
        duration_minutes=20,
        introduction=(
            "Shikantaza is 'just sitting' with bright, open awareness. "
            "There is no object of meditation. No mantra. No visualization. "
            "Simply be fully present, alert, and alive to this moment."
        ),
        body_segments=[
            "Sit with your spine straight, like a stack of coins. "
            "Eyes half-open, gaze resting on the floor a few feet ahead. "
            "Hands in the cosmic mudra. Breathe naturally.",

            "Thoughts will come. Let them. Do not invite them in for tea, "
            "but do not slam the door either. They arrive and they leave. "
            "You are not your thoughts. You are the awareness in which they arise.",

            "Sit like a mountain. Unmoving, yet fully alive. "
            "Every cell alert. Every sense open. "
            "This is not spacing out. It is the most intense form of presence.",

            "There is nothing to achieve. Nowhere to go. Nothing to become. "
            "This moment, exactly as it is, is complete. "
            "You, exactly as you are, are complete. Just sit.",
        ],
        closing=(
            "A bell sounds in the silence. Gently bow. "
            "The meditation is over, and yet it continues. "
            "Every moment is zazen when lived with full presence."
        ),
        focus_areas=["presence", "non-doing", "awareness"],
        difficulty=Difficulty.INTERMEDIATE,
    ),
    GuidedScript(
        id="zazen_02",
        title="Breath Counting Zen",
        style=MeditationStyle.ZAZEN,
        duration_minutes=15,
        introduction=(
            "This is a traditional Zen breath counting practice for developing "
            "concentration (joriki). Simple but demanding. "
            "Each exhale receives a count from one to ten."
        ),
        body_segments=[
            "Take your seat. Spine straight. Eyes softly focused downward. "
            "Settle into stillness for a few breaths.",

            "Begin counting. Exhale: one. Exhale: two. Continue to ten. "
            "If you lose count, return to one without frustration. "
            "This is not failure. It is the practice itself.",

            "The count is a leash for the puppy mind. "
            "Gentle but firm. Each time you return to one, "
            "you are strengthening your capacity for attention.",

            "After reaching ten several times, release the counting. "
            "Sit in the quality of attention that counting has built. "
            "Clear. Sharp. Present.",
        ],
        closing=(
            "Bow gently. This simple practice, done consistently, "
            "builds the foundation for all deeper meditation. "
            "Stand and carry this attention into your next activity."
        ),
        focus_areas=["concentration", "discipline", "Zen practice"],
    ),

    # METTA (1 script)
    GuidedScript(
        id="metta_01",
        title="Boundless Compassion",
        style=MeditationStyle.METTA,
        duration_minutes=15,
        introduction=(
            "Metta is the Pali word for loving-kindness or friendliness. "
            "This practice is one of the oldest meditation techniques, "
            "taught by the Buddha as an antidote to fear."
        ),
        body_segments=[
            "Begin with yourself. Even if it feels awkward. "
            "May I be free from danger. May I be free from mental suffering. "
            "May I be free from physical suffering. May I have ease of well-being.",

            "Bring to mind a benefactor, someone who has helped you. "
            "A teacher, a mentor, a kind stranger. See their face. "
            "Repeat the phrases for them with genuine feeling.",

            "Now think of a friend. Someone you care about. "
            "May you be free from danger. May you have ease of well-being. "
            "Let warmth flow naturally.",

            "Think of a neutral person. Someone you neither like nor dislike. "
            "They deserve the same goodwill. Extend metta to them.",

            "Now, courageously, bring to mind someone difficult. "
            "Start with someone only mildly irritating. "
            "May you be free from suffering. This is for your liberation, not theirs.",

            "Finally, extend metta in all directions. All beings. Without exception. "
            "May all beings be happy. May all beings be free.",
        ],
        closing=(
            "Rest in the warm afterglow of this practice. "
            "Loving-kindness is a muscle. The more you practice, the stronger it grows."
        ),
        focus_areas=["metta", "compassion", "emotional healing"],
    ),
]


class GuidedMeditation:
    """Manages guided meditation sessions."""

    def __init__(self) -> None:
        self._scripts = list(GUIDED_SCRIPTS)

    @property
    def scripts(self) -> list[GuidedScript]:
        """Return all guided scripts."""
        return list(self._scripts)

    @property
    def count(self) -> int:
        """Return the number of available scripts."""
        return len(self._scripts)

    def get_by_id(self, script_id: str) -> Optional[GuidedScript]:
        """Get a specific script by ID."""
        for script in self._scripts:
            if script.id == script_id:
                return script
        return None

    def get_by_style(self, style: MeditationStyle) -> list[GuidedScript]:
        """Get all scripts for a specific meditation style."""
        return [s for s in self._scripts if s.style == style]

    def get_by_difficulty(self, difficulty: Difficulty) -> list[GuidedScript]:
        """Get scripts filtered by difficulty level."""
        return [s for s in self._scripts if s.difficulty == difficulty]

    def get_by_duration(self, max_minutes: int) -> list[GuidedScript]:
        """Get scripts that fit within a time limit."""
        return [s for s in self._scripts if s.duration_minutes <= max_minutes]

    def get_random(self, style: Optional[MeditationStyle] = None) -> GuidedScript:
        """Get a random script, optionally filtered by style."""
        pool = self.get_by_style(style) if style else self._scripts
        if not pool:
            pool = self._scripts
        return random.choice(pool)

    def get_for_mood(self, mood: str) -> list[GuidedScript]:
        """Get scripts recommended for a current mood."""
        mood_lower = mood.lower()
        if mood_lower in ("stressed", "anxious", "tense"):
            styles = [
                MeditationStyle.BREATH_AWARENESS,
                MeditationStyle.BODY_SCAN,
                MeditationStyle.YOGA_NIDRA,
            ]
        elif mood_lower in ("sad", "lonely", "down"):
            styles = [
                MeditationStyle.LOVING_KINDNESS,
                MeditationStyle.METTA,
            ]
        elif mood_lower in ("angry", "frustrated", "irritated"):
            styles = [
                MeditationStyle.LOVING_KINDNESS,
                MeditationStyle.BREATH_AWARENESS,
            ]
        elif mood_lower in ("sleepy", "tired", "exhausted"):
            styles = [
                MeditationStyle.YOGA_NIDRA,
                MeditationStyle.BODY_SCAN,
            ]
        elif mood_lower in ("restless", "scattered"):
            styles = [
                MeditationStyle.ZAZEN,
                MeditationStyle.MANTRA,
            ]
        else:
            styles = [
                MeditationStyle.BREATH_AWARENESS,
                MeditationStyle.VISUALIZATION,
                MeditationStyle.MINDFULNESS,
            ]
        return [s for s in self._scripts if s.style in styles]

    def search(self, query: str) -> list[GuidedScript]:
        """Search scripts by title, focus areas, or content."""
        query_lower = query.lower()
        results = []
        for script in self._scripts:
            searchable = (
                script.title.lower()
                + " " + script.introduction.lower()
                + " " + " ".join(script.focus_areas)
            )
            if query_lower in searchable:
                results.append(script)
        return results

    def get_styles_available(self) -> list[MeditationStyle]:
        """Return all meditation styles that have scripts."""
        return list(set(s.style for s in self._scripts))

    def add_script(self, script: GuidedScript) -> None:
        """Add a custom guided script."""
        self._scripts.append(script)
