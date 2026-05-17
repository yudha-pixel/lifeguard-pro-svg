// Lifeguard Pro — Main Sidebar Shell
// ui_kits/gmail_sidebar/Sidebar.jsx

const TABS = [
  { id: 'preview',     label: 'Preview' },
  { id: 'fulldeal',    label: 'Full Deal' },
  { id: 'org',         label: 'Organization' },
  { id: 'contacts',    label: 'All Contacts' },
  { id: 'chatter',     label: 'Chatter Box' },
];

const EMAIL_CTX = {
  from: 'Franklin Rodriguez',
  email: 'f.rodriguez@redroostercafe.com',
  subject: 'Re: Lifeguard Certification Proposal — Red Rooster Cafe Team',
  snippet: 'Thanks for sending the proposal. We have around 12 staff who need certification by end of Q3.',
};

function ShellCard({ onLoad }) {
  const [loading, setLoading] = React.useState(false);
  function handleLoad() {
    setLoading(true);
    setTimeout(() => { setLoading(false); onLoad(); }, 1200);
  }
  return (
    <div style={{ padding: '12px 12px 16px' }}>
      {/* Logo */}
      <div style={{
        textAlign: 'center',
        padding: '10px 0 12px',
        borderBottom: `1px solid ${COLORS.border}`,
        marginBottom: 12,
      }}>
        <img src="../../assets/lifeguard_pro_logo.png" width="44" height="44"
          alt="Lifeguard Pro" style={{ borderRadius: '50%', display: 'inline-block' }} />
      </div>
      {/* Email context */}
      <FieldPair label="From" value={EMAIL_CTX.from} />
      <FieldPair label="Email" value={EMAIL_CTX.email} />
      <FieldPair label="Subject" value={EMAIL_CTX.subject} />
      <Divider />
      <div style={{ marginTop: 10, marginBottom: 10, fontFamily: bodyStack, fontSize: 12, color: COLORS.textTert, lineHeight: 1.5 }}>
        Deal Quick Info · Contact · Activities · Notes
      </div>
      <div style={{ fontFamily: bodyStack, fontSize: 12, color: COLORS.textTert, marginBottom: 12 }}>
        Click below to load CRM data from Odoo.
      </div>
      {loading ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <div style={{
            width: 14, height: 14, borderRadius: '50%',
            border: `2px solid ${COLORS.terracotta}`,
            borderTopColor: 'transparent',
            animation: 'spin 0.7s linear infinite',
          }} />
          <span style={{ fontFamily: bodyStack, fontSize: 12, color: COLORS.terracotta }}>Loading CRM data…</span>
        </div>
      ) : (
        <FilledBtn label="Load CRM Data" onClick={handleLoad} />
      )}
    </div>
  );
}

function SidebarHeader({ activeTab, onTabChange }) {
  return (
    <div style={{
      borderBottom: `1px solid ${COLORS.border}`,
      background: COLORS.surface1,
    }}>
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '8px 12px 6px',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <img src="../../assets/lifeguard_pro_logo.png" width="24" height="24"
            alt="Lifeguard Pro" style={{ borderRadius: '50%' }} />
          <div>
            <div style={{ fontFamily: "'Myriad Pro','DM Sans',sans-serif", fontSize: 12, fontWeight: 700, color: COLORS.textPri }}>
              Lifeguard Pro CRM
            </div>
            <div style={{ fontFamily: bodyStack, fontSize: 10, color: COLORS.textTert }}>
              Red Rooster Cafe — Group Cert
            </div>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
          <Badge label="QUALIFIED" bg={COLORS.navy + '44'} color={COLORS.mint} />
        </div>
      </div>
      <div style={{
        display: 'flex',
        gap: 1,
        padding: '0 6px 6px',
        overflowX: 'auto',
      }}>
        {TABS.map(t => (
          <button key={t.id} onClick={() => onTabChange(t.id)} style={{
            background: activeTab === t.id ? COLORS.navy : 'transparent',
            color: activeTab === t.id ? '#fff' : COLORS.textTert,
            border: 'none',
            borderRadius: 4,
            padding: '4px 7px',
            fontSize: 10,
            fontFamily: bodyStack,
            fontWeight: activeTab === t.id ? 600 : 400,
            cursor: 'pointer',
            whiteSpace: 'nowrap',
            flexShrink: 0,
          }}>{t.label}</button>
        ))}
      </div>
    </div>
  );
}

function OpportunityBanner() {
  return (
    <div style={{
      background: COLORS.surface1,
      borderBottom: `1px solid ${COLORS.border}`,
      padding: '6px 12px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
    }}>
      <div>
        <div style={{ fontFamily: bodyStack, fontSize: 11, fontWeight: 600, color: COLORS.textSec }}>
          Red Rooster Cafe — Group Certification
        </div>
        <div style={{ fontFamily: bodyStack, fontSize: 10, color: COLORS.textTert, marginTop: 1 }}>
          $12,000 · 45% · Qualified Lead
        </div>
      </div>
      <a href="#" style={{
        fontFamily: bodyStack, fontSize: 10, color: COLORS.terracotta,
        textDecoration: 'none', whiteSpace: 'nowrap',
      }}>Open Odoo ↗</a>
    </div>
  );
}

function RefreshBar({ timestamp }) {
  return (
    <div style={{
      padding: '4px 12px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      borderBottom: `1px solid ${COLORS.border}`,
    }}>
      <span style={{ fontFamily: bodyStack, fontSize: 10, color: COLORS.textTert }}>
        Loaded: {timestamp}
      </span>
      <button style={{
        background: 'transparent', border: 'none', cursor: 'pointer',
        fontFamily: bodyStack, fontSize: 10, color: COLORS.textTert, padding: '2px 4px',
      }}>↻ Refresh</button>
    </div>
  );
}

function Sidebar() {
  const [loaded, setLoaded] = React.useState(false);
  const [tab, setTab] = React.useState('preview');

  const tabContent = {
    preview:  <PreviewTab />,
    fulldeal: <FullDealTab />,
    org:      <OrganizationTab />,
    contacts: <AllContactsTab />,
    chatter:  <ChatterBoxTab />,
  };

  return (
    <div style={{
      width: 300,
      minHeight: '100vh',
      background: COLORS.surface0,
      display: 'flex',
      flexDirection: 'column',
      borderLeft: `1px solid ${COLORS.border}`,
      fontFamily: bodyStack,
    }}>
      <style>{`
        @font-face { font-family:'Myriad Pro'; src:url('../../fonts/MYRIADPRO-BOLD.OTF') format('opentype'); font-weight:700; }
        @keyframes spin { to { transform: rotate(360deg); } }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: ${COLORS.surface1}; }
        ::-webkit-scrollbar-thumb { background: ${COLORS.borderDef}; border-radius: 2px; }
      `}</style>

      {!loaded ? (
        <ShellCard onLoad={() => setLoaded(true)} />
      ) : (
        <>
          <SidebarHeader activeTab={tab} onTabChange={setTab} />
          <OpportunityBanner />
          <RefreshBar timestamp="Mon, May 18 2026 9:42 AM" />
          <div style={{ flex: 1, overflowY: 'auto' }}>
            {tabContent[tab]}
          </div>
        </>
      )}
    </div>
  );
}

Object.assign(window, { Sidebar });
