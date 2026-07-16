import React from 'react';
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  spring,
  interpolate,
} from 'remotion';

// ---- Palette (same brand colors as the other videos) ----
const COLORS = {
  bg: '#FFFFFF',
  border: '#334155',
  boxFill: '#F1F5F9',
  calling: '#2563EB',   // still calling itself
  baseCase: '#059669',  // hit the base case
  unwind: '#D97706',    // returning / unwinding
  danger: '#DC2626',    // infinite loop warning
  text: '#1E293B',
  muted: '#64748B',
};

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
        fontSize: 26,
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

// A single step in the call-stack staircase
const CallStep: React.FC<{
  label: string;
  depth: number;
  state: 'calling' | 'base' | 'unwinding' | 'default' | 'broken';
  appearFrame: number;
}> = ({ label, depth, state, appearFrame }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const localFrame = frame - appearFrame;
  const scale = spring({ frame: localFrame, fps, config: { damping: 12 } });
  const opacity = interpolate(localFrame, [0, 8], [0, 1], { extrapolateRight: 'clamp' });

  const stateColor =
    state === 'calling'
      ? COLORS.calling
      : state === 'base'
      ? COLORS.baseCase
      : state === 'unwinding'
      ? COLORS.unwind
      : state === 'broken'
      ? COLORS.danger
      : COLORS.border;

  return (
    <div
      style={{
        position: 'absolute',
        left: 260 + depth * 130,
        top: 130 + depth * 85,
        width: 260,
        height: 60,
        borderRadius: 12,
        border: `3px solid ${stateColor}`,
        background: state === 'default' ? COLORS.boxFill : `${stateColor}12`,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: 'Arial, sans-serif',
        fontWeight: 700,
        fontSize: 20,
        color: stateColor,
        transform: `scale(${scale})`,
        opacity,
        boxShadow: `0 4px 12px ${stateColor}22`,
      }}
    >
      {label}
      {state === 'base' && (
        <span
          style={{
            position: 'absolute',
            right: -70,
            background: COLORS.baseCase,
            color: '#FFFFFF',
            fontSize: 12,
            fontWeight: 800,
            padding: '4px 10px',
            borderRadius: 999,
          }}
        >
          STOP
        </span>
      )}
    </div>
  );
};

// ---- Scene 1: Hook ----
const HookScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const titleScale = spring({ frame, fps, config: { damping: 12 } });

  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      <div
        style={{
          position: 'absolute',
          top: 160,
          width: '100%',
          textAlign: 'center',
          fontFamily: 'Arial, sans-serif',
          fontSize: 42,
          fontWeight: 800,
          color: COLORS.text,
          transform: `scale(${titleScale})`,
        }}
      >
        Recursion sounds scary. It isn't.
      </div>
      <Caption text="A function that calls itself to solve a smaller version of the same problem." />
    </AbsoluteFill>
  );
};

// ---- Scene 2: Building the staircase down ----
const CallStackDownScene: React.FC = () => {
  const steps = [5, 4, 3, 2, 1];
  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      {steps.map((n, i) => (
        <CallStep
          key={n}
          label={`countdown(${n})`}
          depth={i}
          state="calling"
          appearFrame={i * 12}
        />
      ))}
      <Caption text="Print the number, then call itself with one less. Every time." />
    </AbsoluteFill>
  );
};

// ---- Scene 3: Base case ----
const BaseCaseScene: React.FC = () => {
  const steps = [5, 4, 3, 2, 1];
  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      {steps.map((n, i) => (
        <CallStep key={n} label={`countdown(${n})`} depth={i} state="calling" appearFrame={0} />
      ))}
      <CallStep label="countdown(0)" depth={5} state="base" appearFrame={10} />
      <Caption text="Every recursive call needs a base case — a point where it stops." />
    </AbsoluteFill>
  );
};

// ---- Scene 4: Unwinding back up ----
const UnwindScene: React.FC = () => {
  const frame = useCurrentFrame();
  const steps = [
    { n: 0, depth: 5 },
    { n: 1, depth: 4 },
    { n: 2, depth: 3 },
    { n: 3, depth: 2 },
    { n: 4, depth: 1 },
    { n: 5, depth: 0 },
  ];
  // unwinding happens bottom to top, staggered
  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      {steps.map((s, i) => {
        const unwindStart = i * 12;
        const isUnwinding = frame >= unwindStart;
        return (
          <CallStep
            key={s.n}
            label={s.n === 0 ? 'countdown(0)' : `countdown(${s.n})`}
            depth={s.depth}
            state={s.n === 0 ? 'base' : isUnwinding ? 'unwinding' : 'calling'}
            appearFrame={0}
          />
        );
      })}
      <Caption text="It unwinds back up — each call finishes in reverse order." />
    </AbsoluteFill>
  );
};

// ---- Scene 5: The one rule (broken example) ----
const WarningScene: React.FC = () => {
  const frame = useCurrentFrame();
  const shake = Math.sin(frame * 2.5) * 3;
  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      <CallStep label="doSomething(x)" depth={0} state="broken" appearFrame={0} />
      <div
        style={{
          position: 'absolute',
          left: 260 + shake,
          top: 230,
          fontFamily: 'Arial, sans-serif',
          fontWeight: 800,
          fontSize: 18,
          color: COLORS.danger,
        }}
      >
        ↩ calls itself again with the SAME x
      </div>
      <div
        style={{
          position: 'absolute',
          left: '50%',
          top: 420,
          transform: 'translateX(-50%)',
          background: COLORS.danger,
          color: '#FFFFFF',
          fontFamily: 'Arial, sans-serif',
          fontWeight: 800,
          fontSize: 22,
          padding: '12px 28px',
          borderRadius: 999,
        }}
      >
        STACK OVERFLOW
      </div>
      <Caption text="Every call must move closer to the base case — or it never stops." />
    </AbsoluteFill>
  );
};

// ---- Scene 6: Closer ----
const CloserScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const titleScale = spring({ frame, fps, config: { damping: 10 } });

  return (
    <AbsoluteFill
      style={{ backgroundColor: COLORS.bg, alignItems: 'center', justifyContent: 'center' }}
    >
      <div style={{ transform: `scale(${titleScale})`, textAlign: 'center' }}>
        <div style={{ fontFamily: 'Arial, sans-serif', fontWeight: 800, fontSize: 46, color: COLORS.calling }}>
          Recursion, Explained.
        </div>
        <div style={{ fontFamily: 'Arial, sans-serif', fontSize: 20, color: COLORS.text, marginTop: 12 }}>
          Solve smaller &bull; Know when to stop &bull; Unwind the answer
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ---- Root composition ----
export const RecursionExplainer: React.FC = () => {
  return (
    <>
      <Sequence from={0} durationInFrames={210}>
        <HookScene />
      </Sequence>
      <Sequence from={210} durationInFrames={210}>
        <CallStackDownScene />
      </Sequence>
      <Sequence from={420} durationInFrames={210}>
        <BaseCaseScene />
      </Sequence>
      <Sequence from={630} durationInFrames={240}>
        <UnwindScene />
      </Sequence>
      <Sequence from={870} durationInFrames={150}>
        <WarningScene />
      </Sequence>
      <Sequence from={1020} durationInFrames={150}>
        <CloserScene />
      </Sequence>
    </>
  );
};
