// Lifeguard Pro — Shared Sidebar Primitives
// ui_kits/gmail_sidebar/Components.jsx

const COLORS = {
  obsidian:   '#0A0A0A',
  terracotta: '#E25B45',
  mint:       '#DAFFDE',
  navy:       '#1a2744',
  navyDeep:   '#1A365D',
  steel:      '#2d4a8a',
  slate:      '#415064',
  danger:     '#cc2229',
  activities: '#C63C51',
  notes:      '#C99026',
  chatter:    '#7c3f8c',
  success:    '#188038',
  muted:      '#5f6368',
  surface0:   '#0A0A0A',
  surface1:   '#161616',
  surface2:   '#1e1e1e',
  surface3:   '#252525',
  border:     '#2a2a2a',
  borderDef:  '#333333',
  textPri:    '#FFFFFF',
  textSec:    '#B0B8C4',
  textTert:   '#6B7280',
};

const fontStack = "'Myriad Pro', 'DM Sans', 'Helvetica Neue', sans-serif";
const bodyStack = "'DM Sans', 'Helvetica Neue', sans-serif";
const monoStack = "'JetBrains Mono', monospace";

// ── Divider ──────────────────────────────────────────────────────────────
function Divider() {
  return (
    <div style={{ borderTop: `1px solid ${COLORS.border}`, margin: '8px 0' }} />
  );
}

// ── Section Header  ▸ LABEL ───────────────────────────────────────────────
function SectionHeader({ label, color }) {
  return (
    <div style={{ marginBottom: 8 }}>
      <Divider />
      <div style={{
        fontFamily: bodyStack,
        fontSize: 10,
        fontWeight: 700,
        letterSpacing: '0.1em',
        textTransform: 'uppercase',
        color: color || COLORS.terracotta,
        marginTop: 8,
      }}>
        ▸ {label}
      </div>
    </div>
  );
}

// ── Field Pair ────────────────────────────────────────────────────────────
function FieldPair({ label, value, valueColor, mono }) {
  if (!value) return null;
  return (
    <div style={{ marginBottom: 7 }}>
      <div style={{
        fontFamily: bodyStack,
        fontSize: 10,
        fontWeight: 700,
        color: COLORS.navy,
        letterSpacing: '0.07em',
        textTransform: 'uppercase',
        marginBottom: 2,
      }}>{label}</div>
      <div style={{
        fontFamily: mono ? monoStack : bodyStack,
        fontSize: 12,
        color: valueColor || COLORS.textSec,
        lineHeight: 1.4,
      }}>{value}</div>
    </div>
  );
}

// ── Filled Button ─────────────────────────────────────────────────────────
function FilledBtn({ label, onClick, color, small }) {
  const [hov, setHov] = React.useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{
        background: color || COLORS.navy,
        color: '#fff',
        border: 'none',
        borderRadius: 5,
        padding: small ? '4px 10px' : '7px 14px',
        fontFamily: bodyStack,
        fontSize: small ? 11 : 12,
        fontWeight: 500,
        cursor: 'pointer',
        opacity: hov ? 0.85 : 1,
        transition: 'opacity 0.15s',
        whiteSpace: 'nowrap',
      }}>{label}</button>
  );
}

// ── Ghost Button ──────────────────────────────────────────────────────────
function GhostBtn({ label, onClick, small }) {
  const [hov, setHov] = React.useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{
        background: 'transparent',
        color: COLORS.textTert,
        border: `1px solid ${COLORS.borderDef}`,
        borderRadius: 5,
        padding: small ? '4px 10px' : '7px 14px',
        fontFamily: bodyStack,
        fontSize: small ? 11 : 12,
        fontWeight: 500,
        cursor: 'pointer',
        opacity: hov ? 0.7 : 1,
        transition: 'opacity 0.15s',
        whiteSpace: 'nowrap',
      }}>{label}</button>
  );
}

// ── Badge ─────────────────────────────────────────────────────────────────
function Badge({ label, bg, color }) {
  return (
    <span style={{
      display: 'inline-block',
      background: bg || COLORS.surface2,
      color: color || COLORS.textSec,
      fontSize: 10,
      fontWeight: 600,
      letterSpacing: '0.05em',
      padding: '2px 8px',
      borderRadius: 9999,
      fontFamily: bodyStack,
    }}>{label}</span>
  );
}

// ── Input ─────────────────────────────────────────────────────────────────
function Input({ placeholder, value, multiline, rows }) {
  const [val, setVal] = React.useState(value || '');
  const shared = {
    background: COLORS.surface3,
    border: `1px solid ${COLORS.borderDef}`,
    borderRadius: 4,
    padding: '6px 8px',
    fontFamily: bodyStack,
    fontSize: 12,
    color: COLORS.textSec,
    width: '100%',
    boxSizing: 'border-box',
    outline: 'none',
    resize: 'vertical',
  };
  if (multiline) {
    return <textarea rows={rows || 3} style={shared} value={val} onChange={e => setVal(e.target.value)} placeholder={placeholder} />;
  }
  return <input style={shared} value={val} onChange={e => setVal(e.target.value)} placeholder={placeholder} />;
}

// ── Select ────────────────────────────────────────────────────────────────
function Select({ options, value }) {
  const [val, setVal] = React.useState(value || options[0]);
  return (
    <select
      value={val}
      onChange={e => setVal(e.target.value)}
      style={{
        background: COLORS.surface3,
        border: `1px solid ${COLORS.borderDef}`,
        borderRadius: 4,
        padding: '6px 8px',
        fontFamily: bodyStack,
        fontSize: 12,
        color: COLORS.textSec,
        width: '100%',
        boxSizing: 'border-box',
        outline: 'none',
      }}>
      {options.map(o => <option key={o} value={o}>{o}</option>)}
    </select>
  );
}

// ── Tab Bar ───────────────────────────────────────────────────────────────
function TabBar({ tabs, active, onChange }) {
  return (
    <div style={{
      display: 'flex',
      gap: 2,
      padding: '6px 8px',
      background: COLORS.surface1,
      borderBottom: `1px solid ${COLORS.border}`,
      flexWrap: 'wrap',
    }}>
      {tabs.map(t => (
        <button
          key={t.id}
          onClick={() => onChange(t.id)}
          style={{
            background: active === t.id ? COLORS.navy : 'transparent',
            color: active === t.id ? '#fff' : COLORS.textTert,
            border: 'none',
            borderRadius: 4,
            padding: '4px 8px',
            fontSize: 11,
            fontFamily: bodyStack,
            fontWeight: active === t.id ? 600 : 400,
            cursor: 'pointer',
            whiteSpace: 'nowrap',
          }}>{t.label}</button>
      ))}
    </div>
  );
}

// ── Section Block ─────────────────────────────────────────────────────────
function Section({ children, style }) {
  return (
    <div style={{ padding: '8px 12px', ...style }}>
      {children}
    </div>
  );
}

Object.assign(window, {
  COLORS, fontStack, bodyStack, monoStack,
  Divider, SectionHeader, FieldPair,
  FilledBtn, GhostBtn, Badge, Input, Select,
  TabBar, Section,
});
