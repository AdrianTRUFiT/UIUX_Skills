import { useCallback, useEffect, useState } from "react";
import { getStatus } from "./api";
import type { Status } from "./types";
import { ExplorerScreen } from "./screens/ExplorerScreen";
import { IntakeScreen } from "./screens/IntakeScreen";
import { ReviewQueueScreen } from "./screens/ReviewQueueScreen";
import { SearchScreen } from "./screens/SearchScreen";

const SCREENS = [
  "Evidence Intake",
  "Review Queue",
  "Repository Explorer",
  "Universal Search",
] as const;
type Screen = (typeof SCREENS)[number];

export default function App() {
  const [screen, setScreen] = useState<Screen>("Evidence Intake");
  const [status, setStatus] = useState<Status | null>(null);

  const refreshStatus = useCallback(() => {
    getStatus().then(setStatus).catch(() => setStatus(null));
  }, []);
  useEffect(refreshStatus, [refreshStatus]);

  return (
    <>
      <header className="app-header">
        <h1>
          Evidence Intake Workstation
          {status && <span className="mode-badge" data-testid="mode-badge">{status.mode} mode</span>}
        </h1>
        <div className="subline" data-testid="status-line">
          {status
            ? `${status.counts.proof_objects} Proof Objects · ${status.counts.pending_review} pending review · ` +
              `${status.counts.duplicates} duplicate occurrences · ${status.counts.errors} processing errors`
            : "Connecting to local registry…"}
        </div>
        <nav className="tabs">
          {SCREENS.map((s) => (
            <button
              key={s}
              className={screen === s ? "active" : ""}
              onClick={() => setScreen(s)}
              data-testid={`tab-${s.toLowerCase().replace(/ /g, "-")}`}
            >
              {s}
            </button>
          ))}
        </nav>
      </header>
      <main>
        {screen === "Evidence Intake" && <IntakeScreen onImported={refreshStatus} />}
        {screen === "Review Queue" && <ReviewQueueScreen onChanged={refreshStatus} />}
        {screen === "Repository Explorer" && <ExplorerScreen />}
        {screen === "Universal Search" && <SearchScreen />}
      </main>
    </>
  );
}
