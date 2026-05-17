// Lifeguard Pro — Chatter Box Tab
// ui_kits/gmail_sidebar/ChatterBoxTab.jsx

const MOCK_CHATTER = [
  {
    badge: 'LOG',
    badgeColor: COLORS.chatter,
    author: 'Sarah Mitchell',
    date: 'May 17',
    title: 'Initial call — very interested',
    body: 'Called Franklin, very interested in group cert. Budget approved pending manager sign-off. Will send proposal today.',
  },
  {
    badge: 'EMAIL',
    badgeColor: COLORS.steel,
    author: 'Franklin Rodriguez',
    date: 'May 15',
    title: 'Re: Lifeguard Certification Proposal',
    body: 'Thanks for the info. I\'ve shared it with our team. We have around 12 staff who need certification.',
  },
  {
    badge: 'EMAIL',
    badgeColor: COLORS.steel,
    author: 'Sarah Mitchell',
    date: 'May 14',
    title: 'Lifeguard Certification Proposal — Red Rooster Cafe Team',
    body: 'Hi Franklin, following up on your inquiry about group training packages…',
  },
  {
    badge: 'ACTIVITY',
    badgeColor: COLORS.activities,
    author: 'Marcus Hill',
    date: 'May 13',
    title: 'Initial outreach call scheduled',
    body: 'Set follow-up call for May 15. Lead came in via web form.',
  },
];

function ChatterItem({ item }) {
  const [expanded, setExpanded] = React.useState(false);
  return (
    <div
      onClick={() => setExpanded(!expanded)}
      style={{
        padding: '8px 0',
        borderBottom: `1px solid ${COLORS.border}`,
        cursor: 'pointer',
      }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 3 }}>
        <span style={{
          background: item.badgeColor + '22',
          color: item.badgeColor,
          fontSize: 9,
          fontWeight: 700,
          letterSpacing: '0.06em',
          padding: '1px 6px',
          borderRadius: 3,
          fontFamily: bodyStack,
          border: `1px solid ${item.badgeColor}44`,
        }}>{item.badge}</span>
        <span style={{ fontFamily: bodyStack, fontSize: 11, color: COLORS.textSec, fontWeight: 500 }}>
          {item.author}
        </span>
        <span style={{ fontFamily: bodyStack, fontSize: 10, color: COLORS.textTert, marginLeft: 'auto' }}>
          {item.date}
        </span>
      </div>
      <div style={{ fontFamily: bodyStack, fontSize: 12, color: COLORS.textPri, fontWeight: 500, marginBottom: expanded ? 4 : 0 }}>
        {item.title}
      </div>
      {expanded && (
        <div style={{ fontFamily: bodyStack, fontSize: 11, color: COLORS.textTert, lineHeight: 1.5, marginTop: 4 }}>
          {item.body}
        </div>
      )}
    </div>
  );
}

function ChatterBoxTab() {
  const [note, setNote] = React.useState('');
  const [posted, setPosted] = React.useState(false);

  function handlePost() {
    if (!note.trim()) return;
    setPosted(true);
    setTimeout(() => { setPosted(false); setNote(''); }, 2000);
  }

  return (
    <div>
      {/* Composer */}
      <Section>
        <SectionHeader label="Add Log Note" color={COLORS.chatter} />
        <textarea
          value={note}
          onChange={e => setNote(e.target.value)}
          placeholder="Type a log note…"
          rows={3}
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
            resize: 'vertical',
            marginBottom: 8,
          }}
        />
        {posted ? (
          <Badge label="✓ Note Posted" bg={COLORS.success + '22'} color={COLORS.success} />
        ) : (
          <FilledBtn label="Post Log Note" onClick={handlePost} color={COLORS.navy} />
        )}
      </Section>

      {/* Timeline */}
      <Section>
        <SectionHeader label="Conversation Timeline" color={COLORS.navy} />
        <div style={{ fontSize: 10, color: COLORS.textTert, fontFamily: bodyStack, marginBottom: 8 }}>
          Click any entry to expand
        </div>
        {MOCK_CHATTER.map((item, i) => (
          <ChatterItem key={i} item={item} />
        ))}
      </Section>
    </div>
  );
}

Object.assign(window, { ChatterBoxTab });
