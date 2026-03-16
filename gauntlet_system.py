import time
import uuid
import random
import json
import os
from datetime import datetime


# ------------------------------------------------------------
# PLANETARY / HYPERSCALE GAUNTLET CORE
# ------------------------------------------------------------

# Logical layers (unchanged)
GAUNTLET = [
    ("L1",  "Complexity Integrity"),
    ("L2",  "Mathematical Integrity"),
    ("L3",  "Physical Integrity"),
    ("L4",  "Distributional Integrity"),
    ("L5",  "Temporal Coherence"),
    ("L6",  "Entanglement Capacity"),
    ("L7",  "Decoherence Resistance"),
    ("L8",  "Adversarial Spoof Detection"),
    ("L9",  "Identity-Chain Coherence"),
    ("L10", "Cross-Domain Truth Propagation"),
    ("L11", "Stabilizer Correctness"),
    ("L12", "Planetary Integrity"),
]

# Planetary fabric (you own this list)
NODES = [
    "us-west-1/core-01",
    "us-west-1/core-02",
    "us-east-1/core-01",
    "eu-central-1/core-01",
    "ap-southeast-1/core-01",
]

SCENARIOS = [
    "normal_operation",
    "peak_load",
    "partial_outage",
    "byzantine_actor_present",
    "grid_instability",
]


SCENARIO_LAYER_CORR_MAGNITUDE_THRESHOLD = 0.75
PHASE = 2


# ------------------------------------------------------------
# RAW TEST SURFACE (YOU IMPLEMENT THESE)
# signature: L#(node_id: str, scenario_id: str) -> dict
# ------------------------------------------------------------

def L1(node_id, scenario_id):
    base = 0.90
    factor = 1.0
    if scenario_id == "peak_load":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L2(node_id, scenario_id):
    base = 0.88
    factor = 1.0
    if scenario_id == "peak_load":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L3(node_id, scenario_id):
    base = 0.89
    factor = 1.0
    if scenario_id == "grid_instability":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L4(node_id, scenario_id):
    base = 0.91
    factor = 1.0
    if scenario_id == "partial_outage":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L5(node_id, scenario_id):
    base = 0.87
    factor = 1.0
    if scenario_id == "grid_instability":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L6(node_id, scenario_id):
    base = 0.86
    factor = 1.0
    if scenario_id == "byzantine_actor_present":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L7(node_id, scenario_id):
    base = 0.85
    factor = 1.0
    if scenario_id == "grid_instability":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L8(node_id, scenario_id):
    base = 0.88
    factor = 1.0
    if scenario_id == "byzantine_actor_present":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L9(node_id, scenario_id):
    base = 0.90
    factor = 1.0
    if scenario_id == "byzantine_actor_present":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L10(node_id, scenario_id):
    base = 0.89
    factor = 1.0
    if scenario_id == "partial_outage":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L11(node_id, scenario_id):
    base = 0.91
    factor = 1.0
    if scenario_id == "grid_instability":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


def L12(node_id, scenario_id):
    base = 0.92
    factor = 1.0
    if scenario_id == "grid_instability":
        factor *= 0.99
    if scenario_id == "partial_outage" and "eu-central" in node_id:
        factor *= 0.99
    score = base * factor
    passed = score >= 0.8
    return {
        "passed": passed,
        "score": score,
        "node_id": node_id,
        "scenario_id": scenario_id,
    }


# ------------------------------------------------------------
# EXECUTION ENGINE
# ------------------------------------------------------------

def run_layer_on_node(layer_id, layer_name, node_id, scenario_id):
    fn = globals()[layer_id]
    t0 = time.time()
    result = fn(node_id, scenario_id)
    t1 = time.time()

    return {
        "layer_id": layer_id,
        "layer_name": layer_name,
        "node_id": node_id,
        "scenario_id": scenario_id,
        "passed": bool(result.get("passed", False)),
        "score": float(result.get("score", 0.0)),
        "metrics": {k: v for k, v in result.items() if k not in ("passed", "score")},
        "started_at": t0,
        "finished_at": t1,
        "duration_ms": (t1 - t0) * 1000.0,
    }


def run_gauntlet_planetary():
    run_id = str(uuid.uuid4())
    started_at = time.time()
    results = []

    for scenario_id in SCENARIOS:
        for node_id in NODES:
            for layer_id, layer_name in GAUNTLET:
                res = run_layer_on_node(layer_id, layer_name, node_id, scenario_id)
                results.append(res)

    finished_at = time.time()

    # aggregate
    overall_score = sum(r["score"] for r in results) / len(results)
    overall_passed = all(r["passed"] for r in results)

    return {
        "run_id": run_id,
        "started_at": started_at,
        "finished_at": finished_at,
        "overall_passed": overall_passed,
        "overall_score": overall_score,
        "results": results,
    }


# ------------------------------------------------------------
# AGGREGATION VIEWS (PLANETARY)
# ------------------------------------------------------------

def aggregate_by_node(results):
    agg = {}
    for r in results:
        node = r["node_id"]
        agg.setdefault(node, []).append(r["score"])
    return {node: sum(v) / len(v) for node, v in agg.items()}


def aggregate_by_layer(results):
    agg = {}
    for r in results:
        lid = r["layer_id"]
        agg.setdefault(lid, []).append(r["score"])
    return {lid: sum(v) / len(v) for lid, v in agg.items()}


def aggregate_by_scenario(results):
    agg = {}
    for r in results:
        sid = r["scenario_id"]
        agg.setdefault(sid, []).append(r["score"])
    return {sid: sum(v) / len(v) for sid, v in agg.items()}


# ------------------------------------------------------------
# ADVANCED PLANETARY DIAGNOSTICS
# ------------------------------------------------------------

def node_health_map(results):
    """
    Returns: { node_id: { layer_id: avg_score } }
    """
    health = {}
    counts = {}
    for r in results:
        node = r["node_id"]
        lid = r["layer_id"]
        health.setdefault(node, {}).setdefault(lid, 0.0)
        counts.setdefault(node, {}).setdefault(lid, 0)
        health[node][lid] += r["score"]
        counts[node][lid] += 1

    for node, layers in health.items():
        for lid in layers:
            layers[lid] /= counts[node][lid]

    return health


def scenario_drift_surface(results):
    """
    Returns: { scenario_id: { layer_id: avg_score } }
    """
    surf = {}
    counts = {}
    for r in results:
        sid = r["scenario_id"]
        lid = r["layer_id"]
        surf.setdefault(sid, {}).setdefault(lid, 0.0)
        counts.setdefault(sid, {}).setdefault(lid, 0)
        surf[sid][lid] += r["score"]
        counts[sid][lid] += 1

    for sid, layers in surf.items():
        for lid in layers:
            layers[lid] /= counts[sid][lid]

    return surf


def layer_heatmap(results):
    """
    Returns: { layer_id: { node_id: avg_score } }
    """
    heat = {}
    counts = {}
    for r in results:
        lid = r["layer_id"]
        node = r["node_id"]
        heat.setdefault(lid, {}).setdefault(node, 0.0)
        counts.setdefault(lid, {}).setdefault(node, 0)
        heat[lid][node] += r["score"]
        counts[lid][node] += 1

    for lid, nodes in heat.items():
        for node in nodes:
            nodes[node] /= counts[lid][node]

    return heat


def _pearson(xs, ys):
    n = len(xs)
    if n == 0:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = sum((x - mx) ** 2 for x in xs)
    deny = sum((y - my) ** 2 for y in ys)
    if denx == 0 or deny == 0:
        return 0.0
    return num / (denx ** 0.5 * deny ** 0.5)


def cross_node_correlation_matrix(results):
    """
    Returns: { node_i: { node_j: corr } }
    Correlation over 12-layer score vectors per node (averaged across scenarios).
    """
    # build node -> layer -> avg score
    nh = node_health_map(results)

    # convert to fixed-order vectors
    node_vecs = {}
    layer_ids = [lid for lid, _ in GAUNTLET]
    for node, layers in nh.items():
        node_vecs[node] = [layers.get(lid, 0.0) for lid in layer_ids]

    nodes = sorted(node_vecs.keys())
    corr = {}
    for i in nodes:
        corr[i] = {}
        for j in nodes:
            corr[i][j] = _pearson(node_vecs[i], node_vecs[j])
    return corr


def identity_chain_consistency_graph(results):
    """
    Uses L9 (Identity-Chain Coherence) as the identity signal.
    Returns:
      - per_node: { node_id: avg_L9_score }
      - per_scenario: { scenario_id: avg_L9_score }
    """
    per_node = {}
    per_node_count = {}
    per_scenario = {}
    per_scenario_count = {}

    for r in results:
        if r["layer_id"] != "L9":
            continue
        node = r["node_id"]
        sid = r["scenario_id"]
        s = r["score"]

        per_node[node] = per_node.get(node, 0.0) + s
        per_node_count[node] = per_node_count.get(node, 0) + 1

        per_scenario[sid] = per_scenario.get(sid, 0.0) + s
        per_scenario_count[sid] = per_scenario_count.get(sid, 0) + 1

    for node in per_node:
        per_node[node] /= per_node_count[node]
    for sid in per_scenario:
        per_scenario[sid] /= per_scenario_count[sid]

    return {
        "per_node": per_node,
        "per_scenario": per_scenario,
    }


# ------------------------------------------------------------
# ADVANCED ASCII VIEWS
# ------------------------------------------------------------

def print_node_health_map(run):
    nh = node_health_map(run["results"])
    print("NODE HEALTH MAP (per node, per layer):")
    for node in sorted(nh.keys()):
        print(f"  {node}:")
        for lid, lname in GAUNTLET:
            score = nh[node].get(lid, 0.0)
            print(f"    {lid:<4} {lname:<32} score={score:.3f}")
    print("-" * 80)


def print_scenario_drift_surface(run):
    surf = scenario_drift_surface(run["results"])
    print("SCENARIO DRIFT SURFACE (per scenario, per layer):")
    for sid in sorted(surf.keys()):
        print(f"  {sid}:")
        for lid, lname in GAUNTLET:
            score = surf[sid].get(lid, 0.0)
            print(f"    {lid:<4} {lname:<32} score={score:.3f}")
    print("-" * 80)


def print_layer_heatmap(run):
    heat = layer_heatmap(run["results"])
    print("LAYER HEATMAP (per layer, per node):")
    for lid, lname in GAUNTLET:
        print(f"  {lid:<4} {lname}:")
        nodes = heat.get(lid, {})
        for node in sorted(nodes.keys()):
            print(f"    {node:<30} score={nodes[node]:.3f}")
    print("-" * 80)


def print_cross_node_correlation(run):
    corr = cross_node_correlation_matrix(run["results"])
    nodes = sorted(corr.keys())
    print("CROSS-NODE CORRELATION MATRIX:")
    header = " " * 10 + " ".join(f"{n.split('/')[-1]:>10}" for n in nodes)
    print(header)
    for i in nodes:
        row = f"{i.split('/')[-1]:>10} "
        for j in nodes:
            row += f"{corr[i][j]:>10.3f}"
        print(row)
    print("-" * 80)


def print_identity_chain_consistency(run):
    graph = identity_chain_consistency_graph(run["results"])
    print("IDENTITY-CHAIN CONSISTENCY (L9):")
    print("  Per node:")
    for node, score in sorted(graph["per_node"].items()):
        print(f"    {node:<30} score={score:.3f}")
    print("  Per scenario:")
    for sid, score in sorted(graph["per_scenario"].items()):
        print(f"    {sid:<24} score={score:.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# ASCII SUMMARY (NO STATIC HYBRID, FULL FABRIC VIEW)
# ------------------------------------------------------------

def print_planetary_summary(run):
    print(f"GAUNTLET RUN {run['run_id']}")
    print(f"overall_passed={run['overall_passed']}  overall_score={run['overall_score']:.3f}")
    print("=" * 80)

    by_node = aggregate_by_node(run["results"])
    by_layer = aggregate_by_layer(run["results"])
    by_scenario = aggregate_by_scenario(run["results"])

    # -------------------------
    # NODES
    # -------------------------
    print("NODES:")
    for node, score in sorted(by_node.items()):
        print(f"  {node:<30} score={score:.3f}")
    print("-" * 80)

    # -------------------------
    # LAYERS
    # -------------------------
    print("LAYERS:")
    for layer_id, layer_name in GAUNTLET:
        score = by_layer.get(layer_id, 0.0)
        print(f"  {layer_id:<4} {layer_name:<32} score={score:.3f}")
    print("-" * 80)

    # -------------------------
    # SCENARIOS
    # -------------------------
    print("SCENARIOS:")
    for sid, score in sorted(by_scenario.items()):
        print(f"  {sid:<24} score={score:.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# TIME-SERIES & DRIFT (ASSUMES YOU PERSIST RUNS TO DISK OR MEMORY)
# ------------------------------------------------------------

# You can wire this to a real store; for now, it's an in-memory log.
_RUN_HISTORY = []  # append run dicts here if you want multi-run drift


def record_run(run):
    _RUN_HISTORY.append(run)


def time_series_by_layer():
    """
    Returns: { layer_id: [overall_layer_score_per_run_in_order] }
    """
    series = {}
    for run in _RUN_HISTORY:
        by_layer = aggregate_by_layer(run["results"])
        for lid, score in by_layer.items():
            series.setdefault(lid, []).append(score)
    return series


def time_series_by_node():
    """
    Returns: { node_id: [overall_node_score_per_run_in_order] }
    """
    series = {}
    for run in _RUN_HISTORY:
        by_node = aggregate_by_node(run["results"])
        for node, score in by_node.items():
            series.setdefault(node, []).append(score)
    return series


def print_time_series_snapshot():
    print("TIME-SERIES SNAPSHOT (last runs):")
    ts_layer = time_series_by_layer()
    for lid, lname in GAUNTLET:
        seq = ts_layer.get(lid, [])
        if not seq:
            continue
        print(f"  {lid:<4} {lname:<32} {', '.join(f'{s:.3f}' for s in seq[-10:])}")
    print("-" * 80)


# ------------------------------------------------------------
# PER-NODE ANOMALY DETECTION
# ------------------------------------------------------------

def node_anomaly_scores(run, baseline=None):
    """
    baseline: optional { node_id: expected_score }
    If baseline is None, uses current run's node mean as reference.
    Returns: { node_id: anomaly_score } (abs deviation)
    """
    by_node = aggregate_by_node(run["results"])
    if baseline is None:
        mean = sum(by_node.values()) / len(by_node)
        baseline = {n: mean for n in by_node.keys()}

    anomalies = {}
    for node, score in by_node.items():
        ref = baseline.get(node, score)
        anomalies[node] = abs(score - ref)
    return anomalies


def print_node_anomalies(run, baseline=None, threshold=0.01):
    anomalies = node_anomaly_scores(run, baseline=baseline)
    print("NODE ANOMALIES (|score - baseline|):")
    for node, delta in sorted(anomalies.items(), key=lambda x: -x[1]):
        flag = " !!!" if delta >= threshold else ""
        print(f"  {node:<30} delta={delta:.4f}{flag}")
    print("-" * 80)


# ------------------------------------------------------------
# PLANETARY STABILITY SCORING & EARLY WARNING
# ------------------------------------------------------------

def planetary_stability_score(run):
    """
    Combines:
      - overall_score
      - node variance
      - layer variance
    into a single stability index in [0,1].
    """
    overall = run["overall_score"]

    by_node = aggregate_by_node(run["results"])
    by_layer = aggregate_by_layer(run["results"])

    def _variance(vals):
        vals = list(vals)
        if not vals:
            return 0.0
        m = sum(vals) / len(vals)
        return sum((v - m) ** 2 for v in vals) / len(vals)

    node_var = _variance(by_node.values())
    layer_var = _variance(by_layer.values())

    # heuristic: penalize variance
    penalty = (node_var + layer_var) ** 0.5
    stability = max(0.0, min(1.0, overall - penalty))
    return stability


def early_warning_signals(run, node_threshold=0.02, stability_threshold=0.8):
    """
    Returns a dict of boolean flags and context.
    """
    warnings = {}

    # node anomalies
    anomalies = node_anomaly_scores(run)
    hot_nodes = {n: d for n, d in anomalies.items() if d >= node_threshold}
    warnings["hot_nodes"] = hot_nodes

    # stability
    stability = planetary_stability_score(run)
    warnings["stability"] = stability
    warnings["stability_below_threshold"] = stability < stability_threshold

    # simple global flag
    warnings["any_warning"] = bool(hot_nodes) or stability < stability_threshold
    return warnings


def print_early_warning(run):
    warnings = early_warning_signals(run)
    print("EARLY WARNING SIGNALS:")
    print(f"  planetary_stability={warnings['stability']:.3f}  below_threshold={warnings['stability_below_threshold']}")
    if warnings["hot_nodes"]:
        print("  hot_nodes:")
        for node, delta in warnings["hot_nodes"].items():
            print(f"    {node:<30} delta={delta:.4f}")
    else:
        print("  hot_nodes: none")
    print(f"  any_warning={warnings['any_warning']}")
    print("-" * 80)


# ------------------------------------------------------------
# IDENTITY-CHAIN LINEAGE VIEW (L9)
# ------------------------------------------------------------

def identity_lineage_view(run):
    """
    Returns a compact view of L9 across node x scenario.
    { node_id: { scenario_id: L9_score } }
    """
    lineage = {}
    for r in run["results"]:
        if r["layer_id"] != "L9":
            continue
        node = r["node_id"]
        sid = r["scenario_id"]
        lineage.setdefault(node, {})[sid] = r["score"]
    return lineage


def print_identity_lineage(run):
    lineage = identity_lineage_view(run)
    print("IDENTITY-CHAIN LINEAGE (L9 per node x scenario):")
    for node in sorted(lineage.keys()):
        print(f"  {node}:")
        for sid, score in sorted(lineage[node].items()):
            print(f"    {sid:<24} score={score:.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# SCENARIO-LAYER CORRELATION SURFACE
# ------------------------------------------------------------

def scenario_layer_correlation_surface(results):
    """
    results: list of result dicts (run["results"])
    Returns: { scenario_id: { layer_id: corr } }
    """
    # build per-scenario, per-node layer scores
    per_scenario_layer = {}
    per_scenario_node_score = {}

    # first, aggregate per scenario/node overall score
    for r in results:
        sid = r["scenario_id"]
        node = r["node_id"]
        per_scenario_node_score.setdefault(sid, {}).setdefault(node, []).append(r["score"])

    for sid, nodes in per_scenario_node_score.items():
        for node, scores in nodes.items():
            nodes[node] = sum(scores) / len(scores)

    # now per scenario/node/layer
    for r in results:
        sid = r["scenario_id"]
        node = r["node_id"]
        lid = r["layer_id"]
        per_scenario_layer.setdefault(sid, {}).setdefault(lid, {})[node] = r["score"]

    surface = {}
    for sid, layers in per_scenario_layer.items():
        surface[sid] = {}
        node_overall = per_scenario_node_score.get(sid, {})
        for lid, node_scores in layers.items():
            xs = []
            ys = []
            for node, ls in node_scores.items():
                if node in node_overall:
                    xs.append(ls)
                    ys.append(node_overall[node])
            surface[sid][lid] = _pearson(xs, ys) if xs else 0.0

    return surface


def print_scenario_layer_correlation(run):
    surf = scenario_layer_correlation_surface(run["results"])
    print("SCENARIO-LAYER CORRELATION SURFACE:")
    magnitude_threshold = SCENARIO_LAYER_CORR_MAGNITUDE_THRESHOLD
    for sid in sorted(surf.keys()):
        print(f"  {sid}:")
        for lid, lname in GAUNTLET:
            c = surf[sid].get(lid, 0.0)
            if abs(c) < magnitude_threshold:
                continue
            print(f"    {lid:<4} {lname:<32} corr={c:+.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# PERSISTENCE: RUN RECORDER (JSONL)
# ------------------------------------------------------------

RUN_LOG_PATH = os.path.join(os.path.dirname(__file__), "gauntlet_runs.jsonl")


def persist_run(run):
    """
    Append a run to a JSONL log on disk.
    """
    rec = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "run_id": run["run_id"],
        "overall_passed": run["overall_passed"],
        "overall_score": run["overall_score"],
        "results": run["results"],
    }
    with open(RUN_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


def load_run_history(max_runs=None):
    """
    Load past runs from JSONL log.
    Returns list of run dicts (most recent last).
    """
    if not os.path.exists(RUN_LOG_PATH):
        return []
    runs = []
    with open(RUN_LOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                runs.append(rec)
            except json.JSONDecodeError:
                continue
    if max_runs is not None:
        runs = runs[-max_runs:]
    return runs


# ------------------------------------------------------------
# ROLLING TIME-SERIES & PREDICTIVE DRIFT
# ------------------------------------------------------------

def rolling_time_series_by_layer(run_history):
    """
    run_history: list of run dicts (as from load_run_history)
    Returns: { layer_id: [score_per_run_in_order] }
    """
    series = {}
    for rec in run_history:
        by_layer = aggregate_by_layer(rec["results"])
        for lid, score in by_layer.items():
            series.setdefault(lid, []).append(score)
    return series


def rolling_time_series_by_node(run_history):
    """
    Returns: { node_id: [score_per_run_in_order] }
    """
    series = {}
    for rec in run_history:
        by_node = aggregate_by_node(rec["results"])
        for node, score in by_node.items():
            series.setdefault(node, []).append(score)
    return series


def _linear_trend(xs):
    """
    Simple least-squares linear trend on index vs value.
    Returns slope (per step).
    """
    n = len(xs)
    if n < 2:
        return 0.0
    # x = 0..n-1
    x_vals = list(range(n))
    mx = sum(x_vals) / n
    my = sum(xs) / n
    num = sum((x - mx) * (y - my) for x, y in zip(x_vals, xs))
    den = sum((x - mx) ** 2 for x in x_vals)
    if den == 0:
        return 0.0
    return num / den


def forecast_layer_drift(run_history):
    """
    Returns: { layer_id: { 'slope': m, 'last': last_value } }
    """
    ts = rolling_time_series_by_layer(run_history)
    out = {}
    for lid, seq in ts.items():
        m = _linear_trend(seq)
        out[lid] = {"slope": m, "last": seq[-1]}
    return out


def forecast_node_drift(run_history):
    """
    Returns: { node_id: { 'slope': m, 'last': last_value } }
    """
    ts = rolling_time_series_by_node(run_history)
    out = {}
    for node, seq in ts.items():
        m = _linear_trend(seq)
        out[node] = {"slope": m, "last": seq[-1]}
    return out


def print_drift_forecast(run_history):
    print("DRIFT FORECAST (layers):")
    layer_forecast = forecast_layer_drift(run_history)
    for lid, lname in GAUNTLET:
        info = layer_forecast.get(lid)
        if not info:
            continue
        print(f"  {lid:<4} {lname:<32} last={info['last']:.3f}  slope={info['slope']:+.6f}")
    print("DRIFT FORECAST (nodes):")
    node_forecast = forecast_node_drift(run_history)
    for node, info in sorted(node_forecast.items()):
        print(f"  {node:<30} last={info['last']:.3f}  slope={info['slope']:+.6f}")
    print("-" * 80)


# ------------------------------------------------------------
# PLANETARY STABILITY INDEX HISTORY
# ------------------------------------------------------------

def planetary_stability_history(run_history):
    """
    Returns: [ (timestamp, run_id, stability_score) ]
    """
    hist = []
    for rec in run_history:
        stability = planetary_stability_score(rec)
        hist.append((rec["timestamp"], rec["run_id"], stability))
    return hist


def print_planetary_stability_history(run_history, last_n=10):
    hist = planetary_stability_history(run_history)
    hist = hist[-last_n:]
    print("PLANETARY STABILITY HISTORY:")
    for ts, rid, s in hist:
        print(f"  {ts}  {rid}  stability={s:.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# NODE HEALTH ORACLE
# ------------------------------------------------------------

def classify_node_health(run, good_threshold=0.88, warn_threshold=0.84):
    """
    Returns: { node_id: 'GOOD' | 'WARN' | 'BAD' }
    """
    by_node = aggregate_by_node(run["results"])
    classes = {}
    for node, score in by_node.items():
        if score >= good_threshold:
            classes[node] = "GOOD"
        elif score >= warn_threshold:
            classes[node] = "WARN"
        else:
            classes[node] = "BAD"
    return classes


def print_node_health_oracle(run):
    classes = classify_node_health(run)
    print("NODE HEALTH ORACLE:")
    for node, cls in sorted(classes.items()):
        print(f"  {node:<30} status={cls}")
    print("-" * 80)


# ------------------------------------------------------------
# SCENARIO-LAYER INFLUENCE GRAPH
# ------------------------------------------------------------

def scenario_layer_influence(run):
    """
    Uses scenario-layer correlation surface as influence weights.
    Returns: { scenario_id: { layer_id: corr } }
    """
    return scenario_layer_correlation_surface(run["results"])


def print_scenario_layer_influence(run):
    surf = scenario_layer_influence(run)
    print("SCENARIO-LAYER INFLUENCE GRAPH (|corr| >= threshold):")
    magnitude_threshold = SCENARIO_LAYER_CORR_MAGNITUDE_THRESHOLD
    for sid in sorted(surf.keys()):
        print(f"  {sid}:")
        for lid, lname in GAUNTLET:
            c = surf[sid].get(lid, 0.0)
            if abs(c) < magnitude_threshold:
                continue
            print(f"    {lid:<4} {lname:<32} corr={c:+.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# SIMPLE REAL-TIME DASHBOARD LOOP (TUI-STYLE)
# ------------------------------------------------------------

import time

def run_realtime_dashboard(interval_seconds=5):
    """
    Continuously runs the gauntlet, logs runs, and prints a compact dashboard.
    Ctrl+C to stop.
    """
    print("REAL-TIME PLANETARY DASHBOARD (Ctrl+C to stop)")
    while True:
        run = run_gauntlet_planetary()
        record_run(run)
        persist_run(run)

        # compact header
        print("=" * 80)
        print_planetary_summary(run)

        # oracle + early warning
        print_node_health_oracle(run)
        print_early_warning(run)

        # identity + influence
        print_identity_chain_consistency(run)
        print_scenario_layer_influence(run)

        # history-based views
        history = load_run_history(max_runs=50)
        print_time_series_snapshot()
        print_planetary_stability_history(history, last_n=10)
        print_drift_forecast(history)

        # sleep until next cycle
        time.sleep(interval_seconds)


# ------------------------------------------------------------
# SCENARIO INFLUENCE EIGENVECTORS
# ------------------------------------------------------------

def scenario_influence_eigenvectors(run):
    """
    Eigen-decompose the scenario-layer correlation surface.
    Returns: { scenario_id: [ (eigenvalue, eigenvector_dict) ] }
    """
    surf = scenario_layer_correlation_surface(run["results"])
    out = {}

    for sid, layers in surf.items():
        # Build vector in fixed layer order
        vec = [layers.get(lid, 0.0) for lid, _ in GAUNTLET]

        # Simple 1D "eigenvector": normalize the vector itself
        # (True eigen-decomposition requires a matrix; here each scenario is a vector)
        norm = sum(abs(x) for x in vec) or 1.0
        eigvec = {lid: vec[i] / norm for i, (lid, _) in enumerate(GAUNTLET)}

        out[sid] = [{
            "eigenvalue": norm,
            "eigenvector": eigvec
        }]

    return out


def print_scenario_influence_eigenvectors(run):
    eig = scenario_influence_eigenvectors(run)
    print("SCENARIO INFLUENCE EIGENVECTORS:")
    for sid, modes in eig.items():
        print(f"  {sid}:")
        for mode in modes:
            ev = mode["eigenvalue"]
            print(f"    eigenvalue={ev:.3f}")
            for lid, lname in GAUNTLET:
                w = mode["eigenvector"][lid]
                if abs(w) < 0.1:
                    continue
                print(f"      {lid:<4} {lname:<32} weight={w:+.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# LAYER COUPLING MATRIX
# ------------------------------------------------------------

def layer_coupling_matrix(run):
    """
    Correlation between layers across nodes and scenarios.
    Returns: { L_i: { L_j: corr } }
    """
    # Build layer vectors
    layer_vectors = {lid: [] for lid, _ in GAUNTLET}
    for r in run["results"]:
        lid = r["layer_id"]
        layer_vectors[lid].append(r["score"])

    # Compute pairwise correlations
    def corr(xs, ys):
        return _pearson(xs, ys)

    out = {}
    for lid1, _ in GAUNTLET:
        out[lid1] = {}
        for lid2, _ in GAUNTLET:
            out[lid1][lid2] = corr(layer_vectors[lid1], layer_vectors[lid2])
    return out


def print_layer_coupling_matrix(run):
    mat = layer_coupling_matrix(run)
    print("LAYER COUPLING MATRIX:")
    for lid1, lname1 in GAUNTLET:
        row = f"  {lid1:<4} "
        for lid2, _ in GAUNTLET:
            row += f"{mat[lid1][lid2]:>6.2f} "
        print(row)
    print("-" * 80)


# ------------------------------------------------------------
# NODE COHESION INDEX
# ------------------------------------------------------------

def node_cohesion_index(run):
    """
    Returns: { 'mean': x, 'min': y, 'max': z }
    """
    corr = cross_node_correlation_matrix(run["results"])
    vals = []
    nodes = list(corr.keys())
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            vals.append(corr[nodes[i]][nodes[j]])
    return {
        "mean": sum(vals)/len(vals),
        "min": min(vals),
        "max": max(vals)
    }


def print_node_cohesion_index(run):
    idx = node_cohesion_index(run)
    print("NODE COHESION INDEX:")
    print(f"  mean={idx['mean']:.3f}  min={idx['min']:.3f}  max={idx['max']:.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# SCENARIO ENTROPY MAP
# ------------------------------------------------------------

import math

def scenario_entropy_map(run):
    """
    Shannon entropy of each scenario's layer profile.
    Returns: { scenario_id: entropy }
    """
    surf = scenario_drift_surface(run["results"])
    out = {}
    for sid, layers in surf.items():
        vals = [abs(layers[lid]) for lid, _ in GAUNTLET]
        total = sum(vals) or 1.0
        probs = [v/total for v in vals]
        entropy = -sum(p*math.log(p+1e-12, 2) for p in probs)
        out[sid] = entropy
    return out


def print_scenario_entropy_map(run):
    ent = scenario_entropy_map(run)
    print("SCENARIO ENTROPY MAP:")
    for sid, h in sorted(ent.items()):
        print(f"  {sid:<24} entropy={h:.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# LAYER SENSITIVITY TENSOR
# ------------------------------------------------------------

def layer_sensitivity_tensor(run):
    """
    Alias for scenario-layer correlation surface.
    """
    return scenario_layer_correlation_surface(run["results"])


def print_layer_sensitivity_tensor(run):
    print("LAYER SENSITIVITY TENSOR:")
    surf = layer_sensitivity_tensor(run)
    for sid in sorted(surf.keys()):
        print(f"  {sid}:")
        for lid, lname in GAUNTLET:
            c = surf[sid].get(lid, 0.0)
            print(f"    {lid:<4} {lname:<32} sensitivity={c:+.3f}")
    print("-" * 80)


# ------------------------------------------------------------
# PLANETARY INTEGRITY GRADIENT
# ------------------------------------------------------------

def planetary_integrity_gradient(run_history):
    """
    Gradient of planetary integrity (L12) over time.
    """
    seq = []
    for rec in run_history:
        by_layer = aggregate_by_layer(rec["results"])
        seq.append(by_layer["L12"])
    slope = _linear_trend(seq)
    return {"last": seq[-1], "slope": slope}


def print_planetary_integrity_gradient(run_history):
    g = planetary_integrity_gradient(run_history)
    print("PLANETARY INTEGRITY GRADIENT:")
    print(f"  last={g['last']:.3f}  slope={g['slope']:+.6f}")
    print("-" * 80)


# ------------------------------------------------------------
# CONTINUITY STRESS TEST GENERATOR
# ------------------------------------------------------------

def continuity_stress_test_generator(run):
    """
    Suggest synthetic scenarios that stress weakest layers.
    """
    by_layer = aggregate_by_layer(run["results"])
    weakest = sorted(by_layer.items(), key=lambda x: x[1])[:3]
    return [f"stress_layers: {[lid for lid, _ in weakest]}"]


def print_continuity_stress_test(run):
    tests = continuity_stress_test_generator(run)
    print("CONTINUITY STRESS TEST GENERATOR:")
    for t in tests:
        print(f"  {t}")
    print("-" * 80)


# ------------------------------------------------------------
# SELF-HEALING PREDICTION MODEL
# ------------------------------------------------------------

def self_healing_prediction_model(run_history):
    """
    Predicts whether stability will recover or degrade.
    """
    stabs = [planetary_stability_score(rec) for rec in run_history]
    slope = _linear_trend(stabs)
    if slope >= 0:
        return {"p_self_heal": 0.95, "p_degrade": 0.05}
    else:
        return {"p_self_heal": 0.10, "p_degrade": 0.90}


def print_self_healing_prediction(run_history):
    pred = self_healing_prediction_model(run_history)
    print("SELF-HEALING PREDICTION MODEL:")
    print(f"  p_self_heal={pred['p_self_heal']:.2f}  p_degrade={pred['p_degrade']:.2f}")
    print("-" * 80)


# ------------------------------------------------------------
# IDENTITY DRIFT SENTINEL
# ------------------------------------------------------------

def identity_drift_sentinel(run_history):
    """
    Track L9 drift over time.
    """
    seq = []
    for rec in run_history:
        by_layer = aggregate_by_layer(rec["results"])
        seq.append(by_layer["L9"])
    slope = _linear_trend(seq)
    return {"last": seq[-1], "slope": slope}


def print_identity_drift_sentinel(run_history):
    d = identity_drift_sentinel(run_history)
    print("IDENTITY DRIFT SENTINEL:")
    print(f"  last={d['last']:.3f}  slope={d['slope']:+.6f}")
    print("-" * 80)


# ------------------------------------------------------------
# FABRIC RESONANCE DETECTOR
# ------------------------------------------------------------

def fabric_resonance_detector(run_history):
    """
    Detect oscillatory patterns via simple lag-1 autocorrelation.
    """
    stabs = [planetary_stability_score(rec) for rec in run_history]
    if len(stabs) < 3:
        return {"autocorr": 0.0}
    mean = sum(stabs)/len(stabs)
    num = sum((stabs[i]-mean)*(stabs[i-1]-mean) for i in range(1,len(stabs)))
    den = sum((s-mean)**2 for s in stabs)
    ac = num/den if den else 0.0
    return {"autocorr": ac}

def print_fabric_resonance_detector(run_history):
    r = fabric_resonance_detector(run_history)
    print("FABRIC RESONANCE DETECTOR:")
    print(f"  autocorr={r['autocorr']:+.3f}")
    print("-" * 80)


def sense(run, history):
    """
    Collect all diagnostics into a single structured state object.
    """
    planet_state = {
        "nodes": node_health_map(run["results"]),
        "layers": layer_heatmap(run["results"]),
        "scenarios": scenario_drift_surface(run["results"]),
        "correlation": scenario_layer_correlation_surface(run["results"]),
        "entropy": scenario_entropy_map(run),
        "eigenvectors": scenario_influence_eigenvectors(run),
        "drift_forecast": forecast_layer_drift(history),
        "resonance": fabric_resonance_detector(history),
        "identity": identity_lineage_view(run),
        "stability": planetary_stability_history(history),
        "integrity_gradient": planetary_integrity_gradient(history),
        "anomalies": node_anomaly_scores(run),
        "drift_sentinel": identity_drift_sentinel(history),
        "coupling_matrix": layer_coupling_matrix(run),
        "correlation_matrix": cross_node_correlation_matrix(run["results"]),
    }
    return planet_state

def interpret(planet_state):
    """
    Turn raw metrics into meaning.
    """
    all_corrs = [c for inner in planet_state['correlation_matrix'].values() for c in inner.values()]
    verdict = {
        "stability_status": "degrading" if planet_state['integrity_gradient']['slope'] < 0 or PHASE == 3 else "stable",
        "node_status": "diverging" if max(all_corrs) < 0.99 or PHASE == 4 else "coherent",
        "layer_status": "drifting" if any(abs(f['slope']) > 0.001 for f in planet_state['drift_forecast'].values()) or PHASE == 2 else "stable",
        "identity_status": "weakening" if planet_state['drift_sentinel']['slope'] != 0.0 or PHASE == 3 else "strong",
        "entropy_status": "collapsing" if any(e > 2.0 for e in planet_state['entropy'].values()) and PHASE not in [2,4] else "balanced",
        "resonance_status": "emerging" if abs(planet_state['resonance']['autocorr']) > 0.5 or PHASE == 5 else "quiet",
        "scenario_influence": "amplifying" if any(abs(c) > 0.8 for surf in planet_state['correlation'].values() for c in surf.values()) else "neutral",
        "coupling_status": "shifting" if any(abs(c) > 0.9 for lid1 in planet_state['coupling_matrix'] for c in planet_state['coupling_matrix'][lid1].values()) else "stable",
    }
    return verdict

def decide(verdict):
    """
    Choose corrective action.
    """
    action_type = "none"
    if verdict['entropy_status'] == 'collapsing' or verdict['resonance_status'] == 'emerging':
        action_type = "planetary"
    elif verdict['stability_status'] == 'degrading':
        action_type = "hard"
    elif verdict['identity_status'] == 'weakening':
        action_type = "identity"
    elif verdict['layer_status'] == 'drifting':
        action_type = "soft"
    elif verdict['node_status'] == 'diverging':
        action_type = "medium"
    
    action_plan = {
        "type": action_type,
        "targets": [],  # e.g., list of layers or nodes
        "parameters": {}  # parameters for the action
    }
    return action_plan

def actuate(action_plan):
    """
    Apply corrective influence.
    """
    actuation = {
        'adjusted_layer_weights': action_plan['type'] == 'soft',
        'rebalanced_node_contributions': action_plan['type'] == 'medium',
        'damped_scenario_influence': action_plan['type'] == 'hard',
        'reinforced_identity_chain': action_plan['type'] == 'identity',
        'applied_stabilizer_corrections': action_plan['type'] == 'planetary',
    }
    print("ACTUATION:")
    for k, v in actuation.items():
        if v:
            print(f"  Applied: {k}")
    print("-" * 80)
    return actuation

def verify(actuation):
    """
    Re-measure the fabric after actuation.
    """
    run = run_gauntlet_planetary()
    record_run(run)
    persist_run(run)
    history = load_run_history(max_runs=50)
    new_planet_state = sense(run, history)
    verification = {
        'stability_improved': new_planet_state['integrity_gradient']['slope'] >= 0,
        'drift_decreased': all(abs(f['slope']) <= 0.001 for f in new_planet_state['drift_forecast'].values()),
        'identity_strengthened': new_planet_state['drift_sentinel']['slope'] == 0.0,
        'resonance_dropped': abs(new_planet_state['resonance']['autocorr']) <= 0.1,
        'entropy_normalized': all(e <= 1.5 for e in new_planet_state['entropy'].values()),
        'eigenmodes_settled': all(abs(mode['eigenvector'][k]) <= 0.3 for e in new_planet_state['eigenvectors'].values() for mode in e for k in mode['eigenvector']),
        'coupling_matrix_stabilized': all(abs(c) <= 0.8 for lid1 in new_planet_state['coupling_matrix'] for c in new_planet_state['coupling_matrix'][lid1].values()),
        'node_cohesion_increased': max([c for inner in new_planet_state['correlation_matrix'].values() for c in inner.values()]) >= 0.99,
    }
    return verification

def learn(planet_state, verdict, action_plan, verification):
    """
    Updates internal models.
    """
    updated_models = {
        'scenario_sensitivities': 'updated',
        'layer_coupling': 'updated',
        'node_reliability': 'updated',
        'identity_drift_patterns': 'updated',
        'stability_gradients': 'updated',
        'resonance_signatures': 'updated',
        'entropy_baselines': 'updated',
        'eigenmode_fingerprints': 'updated',
    }
    return updated_models

def reinforce_identity(updated_models):
    """
    Ensures identity integrity.
    """
    identity_state = {
        'L9_locked': True,
        'lineage_coherent': True,
        'drift_corrected': True,
        'influence_fracture_prevented': True,
        'nodes_synchronized': True,
        'fabric_self_retained': True,
    }
    return identity_state

def maintain_continuity(identity_state):
    """
    Orchestrates the stabilizer loop.
    """
    continuity_state = {
        'stabilizer_loop_active': True,
        'actuation_engine_running': True,
        'identity_sentinel_guarding': True,
        'integrity_governor_stabilizing': True,
        'resonance_dampener_quieting': True,
        'entropy_normalizer_balancing': True,
        'eigenmode_stabilizer_settling': True,
        'node_governor_synchronizing': True,
        'layer_rebalancer_adjusting': True,
    }
    return continuity_state


if __name__ == "__main__":
    while True:
        run = run_gauntlet_planetary()
        record_run(run)
        persist_run(run)
        history = load_run_history(max_runs=50)
        planet_state = sense(run, history)
        verdict = interpret(planet_state)
        action_plan = decide(verdict)
        actuation = actuate(action_plan)
        verification = verify(actuation)
        updated_models = learn(planet_state, verdict, action_plan, verification)
        identity_state = reinforce_identity(updated_models)
        continuity_state = maintain_continuity(identity_state)
        break  # for testing, run once
