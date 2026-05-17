// Lifeguard Pro — Full Deal & Organization Tabs
// ui_kits/gmail_sidebar/FullDealTab.jsx

function FullDealTab() {
  return (
    <div>
      <Section>
        <SectionHeader label="Activities" color={COLORS.activities} />
        {MOCK_LEAD.activities.map((a, i) => (
          <div key={i} style={{ marginBottom: 7, padding: '6px 8px', background: COLORS.surface2, borderRadius: 4 }}>
            <div style={{ fontFamily: bodyStack, fontSize: 11, fontWeight: 600, color: COLORS.textSec }}>
              {a.type} · {a.deadline} · {a.user}
            </div>
            <div style={{ fontFamily: bodyStack, fontSize: 11, color: COLORS.textTert, marginTop: 2 }}>{a.summary}</div>
          </div>
        ))}
        <GhostBtn label="Quick Add Activity" small />
      </Section>

      <Section>
        <SectionHeader label="Notes" color={COLORS.notes} />
        <Input multiline rows={3} value={MOCK_LEAD.notes} />
        <div style={{ marginTop: 6 }}><FilledBtn label="Save Notes" small /></div>
      </Section>

      <Section>
        <SectionHeader label="Deal" color={COLORS.navy} />
        <div style={{ marginBottom: 6 }}>
          <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>Stage (Edit)</div>
          <Select options={['Qualified Lead','Proposal Sent','Negotiation','Closed Won','Closed Lost']} value="Qualified Lead" />
        </div>
        <div style={{ marginBottom: 6 }}>
          <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>Opportunity Name (Edit)</div>
          <Input value={MOCK_LEAD.name} />
        </div>
        <div style={{ marginBottom: 6 }}>
          <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>Expected Revenue (Edit)</div>
          <Input value="12000" />
        </div>
        <div style={{ marginBottom: 6 }}>
          <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>Probability (Edit)</div>
          <Input value="45" />
        </div>
      </Section>

      <Section>
        <SectionHeader label="Team" color={COLORS.steel} />
        <FieldPair label="Company (internal)" value="Lifeguard Pro" />
        <FieldPair label="Salesperson" value="Sarah Mitchell" />
        <FieldPair label="Email Setter" value={MOCK_LEAD.emailSetter} />
        <FieldPair label="Phone Setter" value={MOCK_LEAD.phoneSetter} />
        <FieldPair label="Closer" value={MOCK_LEAD.closer} />
      </Section>

      <Section>
        <SectionHeader label="Contact Info" color={COLORS.navy} />
        <div style={{ marginBottom: 6 }}>
          <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>Email (Edit)</div>
          <Input value={MOCK_LEAD.email} />
        </div>
        <div style={{ marginBottom: 6 }}>
          <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>Phone (Edit)</div>
          <Input value={MOCK_LEAD.phone} />
        </div>
        <FieldPair label="Timezone" value={MOCK_LEAD.timezone} />
        <div style={{ padding: '4px 0', borderBottom: `1px solid ${COLORS.border}` }}>
          <span style={{ fontFamily: bodyStack, fontSize: 11, color: COLORS.textTert }}>Contact Rules</span>
          <span style={{ float: 'right' }}>
            <Badge label="ACTIVE" bg={COLORS.success + '22'} color={COLORS.success} />
          </span>
        </div>
      </Section>

      <Section>
        <SectionHeader label="Deal Details" color={COLORS.navy} />
        <FieldPair label="Deal Labels" value={MOCK_LEAD.dealLabels} />
        <FieldPair label="Seeking" value={MOCK_LEAD.seeking} />
        <FieldPair label="Lead Source" value="Web Form" />
        <FieldPair label="Payment Method" value="Invoice" />
      </Section>

      <Section style={{ paddingBottom: 16 }}>
        <FilledBtn label="Save Full Deal" />
      </Section>
    </div>
  );
}

function OrganizationTab() {
  return (
    <div>
      <Section>
        <SectionHeader label="Organization" color={COLORS.slate} />
        <FieldPair label="Company Name" value="Red Rooster Cafe" />
        <FieldPair label="Website" value="redroostercafe.com" />
        <FieldPair label="Industry" value="Hospitality / Food Service" />
        <FieldPair label="City" value="Los Angeles, CA" />
        <FieldPair label="Phone" value="+1 (555) 340-0012" />
        <FieldPair label="Email" value="info@redroostercafe.com" />
      </Section>
      <Section style={{ paddingBottom: 16 }}>
        <FilledBtn label="Save Organization" />
      </Section>
    </div>
  );
}

function AllContactsTab() {
  const contacts = [
    { name: 'Franklin Rodriguez', role: 'Manager', email: 'f.rodriguez@redroostercafe.com' },
    { name: 'Maria Santos', role: 'HR Director', email: 'm.santos@redroostercafe.com' },
  ];
  return (
    <div>
      <Section>
        <SectionHeader label="All Contacts" color={COLORS.slate} />
        {contacts.map((c, i) => (
          <div key={i} style={{ padding: '8px 0', borderBottom: `1px solid ${COLORS.border}` }}>
            <div style={{ fontFamily: bodyStack, fontSize: 12, fontWeight: 600, color: COLORS.textPri }}>{c.name}</div>
            <div style={{ fontFamily: bodyStack, fontSize: 11, color: COLORS.textTert, marginTop: 1 }}>{c.role}</div>
            <div style={{ fontFamily: bodyStack, fontSize: 11, color: COLORS.terracotta, marginTop: 1 }}>{c.email}</div>
          </div>
        ))}
      </Section>
    </div>
  );
}

Object.assign(window, { FullDealTab, OrganizationTab, AllContactsTab });
