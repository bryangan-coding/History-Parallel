export default function SourceList({ sourceIds }: { sourceIds: string[] }) {
  if (sourceIds.length === 0) return null;

  return (
    <div className="mt-6 pt-6 border-t border-stone-200">
      <h4 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
        来源 ({sourceIds.length})
      </h4>
      <ul className="space-y-2">
        {sourceIds.map((sid, idx) => (
          <li key={sid} className="text-sm text-stone-600">
            <span className="text-stone-400 text-xs mr-1.5 tabular-nums">
              [{idx + 1}]
            </span>
            {/* Plain text source note - in production, resolve from source data */}
            {sid === 'src-ztzy' && '司马光等，《资治通鉴》（1084年），Public Domain'}
            {sid === 'src-ss' && '脱脱等，《宋史》（1345年），元朝官修，Public Domain'}
            {sid === 'src-xzsl' && '李焘，《续资治通鉴长编》（1183年），Public Domain'}
            {sid === 'src-domesday' && 'William I Commissioners, Domesday Book (1086), Public Domain'}
            {sid === 'src-asc' && 'Anglo-Saxon Chronicle, Public Domain'}
            {sid === 'src-alexiad' && 'Anna Komnene, The Alexiad (1148), Public Domain'}
            {sid === 'src-papal' && 'Papal Registers of Gregory VII, Public Domain'}
            {sid === 'src-eiga' && '赤染卫门（推定），《荣花物语》（1028年），Public Domain'}
            {sid === 'src-seljuk' && 'J.A. Boyle (ed.), Cambridge History of Iran, Vol. 5 (1968), Copyright'}
            {sid === 'src-byz-empire' && 'Warren Treadgold, A History of the Byzantine State and Society (1997), Copyright'}
            {sid === 'src-chola' && 'K.A. Nilakanta Sastri, The Cholas (1955), Copyright'}
            {sid === 'src-prosop' && 'Prosopography of the Later Roman Empire (1980), Copyright'}
          </li>
        ))}
      </ul>
    </div>
  );
}
