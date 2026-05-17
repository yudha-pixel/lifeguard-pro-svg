// Lifeguard Pro — Preview Tab
// ui_kits/gmail_sidebar/PreviewTab.jsx

const MOCK_LEAD = {
  name: 'Red Rooster Cafe — Group Certification',
  stage: 'Qualified Lead',
  probability: '45%',
  expectedRevenue: '$12,000',
  company: 'Red Rooster Cafe',
  contactName: 'Franklin Rodriguez',
  phone: '+1 (555) 342-7891',
  email: 'f.rodriguez@redroostercafe.com',
  timezone: 'America/Los_Angeles',
  emailSetter: 'Marcus Hill',
  phoneSetter: 'Dana Chen',
  closer: 'Sarah Mitchell',
  dealLabels: 'Group Training, High Priority',
  seeking: 'Lifeguard Cert, First Aid',
  notes: 'Interested in group certification for 12 staff. Budget approved pending manager sign-off. Follow up re: proposal sent 5/17.',
  activities: [
    { type: 'Email', deadline: 'May 20', user: 'Sarah M.', summary: 'Follow up on proposal' },
    { type: 'Call', deadline: 'May 22', user: 'Marcus H.', summary: 'Confirm roster count' },
  ],
};

function ActivitiesSection() {
  const [showAdd, setShowAdd] = React.useState(false);
  return (
    <Section>
      <SectionHeader label="Activities" color={COLORS.activities} />
      {MOCK_LEAD.activities.map((a, i) => (
        <div key={i} style={{ marginBottom: 7 }}>
          <div style={{ fontFamily: bodyStack, fontSize: 11, fontWeight: 600, color: COLORS.textSec }}>
            {a.type} · {a.deadline} · {a.user}
          </div>
          <div style={{ fontFamily: bodyStack, fontSize: 11, color: COLORS.textTert, marginTop: 1 }}>
            {a.summary}
          </div>
        </div>
      ))}
      {showAdd ? (
        <div style={{ marginTop: 8, display: 'flex', flexDirection: 'column', gap: 6 }}>
          <Input placeholder="Activity summary…" />
          <div style={{ display: 'flex', gap: 6 }}>
            <FilledBtn label="Add" small color={COLORS.activities} onClick={() => setShowAdd(false)} />
            <GhostBtn label="Cancel" small onClick={() => setShowAdd(false)} />
          </div>
        </div>
      ) : (
        <div style={{ marginTop: 6 }}>
          <GhostBtn label="Quick Add Activity" small onClick={() => setShowAdd(true)} />
        </div>
      )}
    </Section>
  );
}

function NotesSection() {
  return (
    <Section>
      <SectionHeader label="Notes" color={COLORS.notes} />
      <div style={{ marginBottom: 6 }}>
        <Input multiline rows={3} value={MOCK_LEAD.notes} placeholder="Enter notes…" />
      </div>
      <FilledBtn label="Save Notes" small />
    </Section>
  );
}

function DealQuickInfoSection() {
  return (
    <Section>
      <SectionHeader label="Deal Quick Info" color={COLORS.navy} />
      <div style={{ marginBottom: 6 }}>
        <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>
          Stage (Edit)
        </div>
        <Select options={['Qualified Lead', 'Proposal Sent', 'Negotiation', 'Closed Won', 'Closed Lost']} value="Qualified Lead" />
      </div>
      <div style={{ marginBottom: 6 }}>
        <div style={{ fontFamily: bodyStack, fontSize: 10, fontWeight: 700, color: COLORS.navy, letterSpacing: '0.07em', textTransform: 'uppercase', marginBottom: 4 }}>
          Deal Title (Edit)
        </div>
        <Input value={MOCK_LEAD.name} />
      </div>
      <FieldPair label="Expected Revenue" value={MOCK_LEAD.expectedRevenue} valueColor={COLORS.mint} />
      <FieldPair label="Probability" value={MOCK_LEAD.probability} />
      <FieldPair label="Deal Labels" value={MOCK_LEAD.dealLabels} />
      <FieldPair label="Seeking" value={MOCK_LEAD.seeking} />
    </Section>
  );
}

function TeamSection() {
  return (
    <Section>
      <SectionHeader label="Team" color={COLORS.steel} />
      <FieldPair label="Email Setter" value={MOCK_LEAD.emailSetter} />
      <FieldPair label="Phone Setter" value={MOCK_LEAD.phoneSetter} />
      <FieldPair label="Closer" value={MOCK_LEAD.closer} />
    </Section>
  );
}

function ContactSection() {
  return (
    <Section>
      <SectionHeader label="Contact Quick-Access" color={COLORS.danger} />
      <FieldPair label="Contact Name" value={MOCK_LEAD.contactName} />
      <FieldPair label="Phone (Edit)" value={MOCK_LEAD.phone} />
      <FieldPair label="Email (Edit)" value={MOCK_LEAD.email} />
      <FieldPair label="Timezone" value={MOCK_LEAD.timezone} />
    </Section>
  );
}

function SaveSection() {
  return (
    <Section style={{ paddingBottom: 16 }}>
      <FilledBtn label="Save Quick Deal Info" />
    </Section>
  );
}

function PreviewTab() {
  return (
    <div>
      <ActivitiesSection />
      <NotesSection />
      <DealQuickInfoSection />
      <TeamSection />
      <ContactSection />
      <SaveSection />
    </div>
  );
}

Object.assign(window, { PreviewTab, MOCK_LEAD });
