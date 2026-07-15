import React from 'react';
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  spring,
  interpolate,
} from 'remotion';

// ---- Palette (same brand colors as the Manim white-canvas version) ----
const COLORS = {
  bg: '#FFFFFF',
  border: '#334155',
  boxFill: '#F1F5F9',
  hash: '#2563EB',
  alice: '#059669',
  bob: '#EA580C',
  collision: '#DC2626',
  text: '#1E293B',
  highlight: '#D97706',
  muted: '#64748B',
};

// ---- Reusable caption bar ----
const Caption: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: 'clamp' });
  return (
    <div
      style={{
        position: 'absolute',
        bottom: 60,
        left: '50%',
        transform: 'translateX(-50%)',
        width: '80%',
        background: '#F8FAFC',
        border: `1px solid ${COLORS.border}`,
        borderRadius: 16,
        padding: '20px 32px',
        textAlign: 'center',
        fontSize: 28,
        fontFamily: 'Arial, sans-serif',
        color: COLORS.text,
        opacity,
        boxShadow: '0 4px 20px rgba(0,0,0,0.06)',
      }}
    >
      {text}
    </div>
  );
};

// ---- A single array slot box ----
const ArraySlot: React.FC<{ index: number; x: number; highlight?: string; label?: string }> = ({
  index,
  x,
  highlight,
  label,
}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: 300,
      width: 90,
      height: 90,
      borderRadius: 12,
      border: `3px solid ${highlight || COLORS.border}`,
      background: highlight ? `${highlight}15` : COLORS.boxFill,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: 'Arial, sans-serif',
    }}
  >
    {label && (
      <span style={{ color: highlight, fontWeight: 700, fontSize: 16 }}>{label}</span>
    )}
    <span style={{ position: 'absolute', bottom: -28, color: COLORS.muted, fontSize: 14 }}>
      {index}
    </span>
  </div>
);

// ---- Scene 1: Hook + array intro ----
const HookScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const titleSpring = spring({ frame, fps, config: { damping: 12 } });
  const arrayOpacity = interpolate(frame, [40, 60], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      <div
        style={{
          position: 'absolute',
          top: 100,
          width: '100%',
          textAlign: 'center',
          fontFamily: 'Arial, sans-serif',
          fontSize: 44,
          fontWeight: 800,
          color: COLORS.text,
          transform: `scale(${titleSpring})`,
        }}
      >
        Ever wonder how your phone finds a contact instantly?
      </div>

      <div style={{ opacity: arrayOpacity }}>
        {Array.from({ length: 10 }).map((_, i) => (
          <ArraySlot key={i} index={i} x={340 + i * 105} />
        ))}
      </div>

      <Caption text="That's a hash map. Let's break it down." />
    </AbsoluteFill>
  );
};

// ---- Scene 2: Hash function + Alice ----
const HashFunctionScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Alice key moves into the hash box, then output "7" springs out
  const keyX = interpolate(frame, [0, 30], [200, 640], { extrapolateRight: 'clamp' });
  const keyOpacity = interpolate(frame, [25, 35], [1, 0], { extrapolateRight: 'clamp' });
  const outputScale = spring({ frame: frame - 35, fps, config: { damping: 10 } });

  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      {Array.from({ length: 10 }).map((_, i) => (
        <ArraySlot key={i} index={i} x={340 + i * 105} />
      ))}

      <div
        style={{
          position: 'absolute',
          left: 600,
          top: 120,
          width: 220,
          height: 100,
          borderRadius: 16,
          border: `3px solid ${COLORS.hash}`,
          background: '#EFF6FF',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontFamily: 'Arial, sans-serif',
          fontWeight: 700,
          color: COLORS.hash,
          fontSize: 20,
          boxShadow: '0 6px 18px rgba(37,99,235,0.15)',
        }}
      >
        Hash Function
      </div>

      <div
        style={{
          position: 'absolute',
          left: keyX,
          top: 155,
          opacity: keyOpacity,
          fontFamily: 'Arial, sans-serif',
          fontWeight: 700,
          fontSize: 24,
          color: COLORS.alice,
        }}
      >
        Alice
      </div>

      {frame > 35 && (
        <div
          style={{
            position: 'absolute',
            left: 870,
            top: 130,
            transform: `scale(${outputScale})`,
            fontFamily: 'Arial, sans-serif',
            fontWeight: 800,
            fontSize: 48,
            color: COLORS.alice,
          }}
        >
          7
        </div>
      )}

      <Caption text="The hash function turns 'Alice' into a number." />
    </AbsoluteFill>
  );
};

// ---- Scene 3: Collision ----
const CollisionScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const shake = Math.sin(frame * 2) * (frame < 20 ? 4 : 0);
  const badgeScale = spring({ frame, fps, config: { damping: 8 } });

  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      {Array.from({ length: 10 }).map((_, i) => (
        <ArraySlot
          key={i}
          index={i}
          x={340 + i * 105 + (i === 7 ? shake : 0)}
          highlight={i === 7 ? COLORS.collision : undefined}
          label={i === 7 ? 'Alice + Bob' : undefined}
        />
      ))}

      <div
        style={{
          position: 'absolute',
          left: '50%',
          top: 460,
          transform: `translateX(-50%) scale(${badgeScale})`,
          background: COLORS.collision,
          color: '#FFFFFF',
          fontFamily: 'Arial, sans-serif',
          fontWeight: 800,
          fontSize: 28,
          padding: '14px 32px',
          borderRadius: 999,
        }}
      >
        COLLISION!
      </div>

      <Caption text="Two keys hashed to the same slot — 7." />
    </AbsoluteFill>
  );
};

// ---- Scene 4: Closer ----
const CloserScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const titleScale = spring({ frame, fps, config: { damping: 10 } });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: COLORS.bg,
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <div style={{ transform: `scale(${titleScale})`, textAlign: 'center' }}>
        <div style={{ fontFamily: 'Arial, sans-serif', fontWeight: 800, fontSize: 48, color: COLORS.hash }}>
          Hash Maps, Explained.
        </div>
        <div style={{ fontFamily: 'Arial, sans-serif', fontSize: 22, color: COLORS.text, marginTop: 12 }}>
          O(1) Lookups &bull; Collision Chaining
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ---- Root composition: stitches scenes together on the timeline ----
export const HashMapExplainer: React.FC = () => {
  return (
    <>
      <Sequence from={0} durationInFrames={210}>
        <HookScene />
      </Sequence>
      <Sequence from={210} durationInFrames={240}>
        <HashFunctionScene />
      </Sequence>
      <Sequence from={450} durationInFrames={240}>
        <CollisionScene />
      </Sequence>
      <Sequence from={690} durationInFrames={90}>
        <CloserScene />
      </Sequence>
    </>
  );
};
