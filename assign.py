
import networkx as nx

class Node(object):
    def __init__(self, subtype, nid):
        self.subtype = subtype
        self.nid = nid

def build_graph(reviewers, papers, conflicts):
    g = nx.DiGraph()

    reviewer_nodes = {n: Node('reviewer', n) for n in reviewers}
    paper_nodes = {n: Node('paper', n) for n in papers}

    source = Node('super_source', 'source')
    sink = Node('super_sink', 'sink')

    g.add_node(source)
    g.add_node(sink)

    for n in reviewers:
        cap = reviewers[n]['number-of-papers']
        rn = reviewer_nodes[n]
        g.add_edge(source, rn, capacity=cap)

    for n in papers:
        cap = papers[n]['number-of-reviews']
        pn = paper_nodes[n]
        g.add_edge(pn, sink, capacity=cap)

    for rn in reviewers:
        for pn in papers:
            if (rn, pn) in conflicts:
                continue
            n1 = reviewer_nodes[rn]
            n2 = paper_nodes[pn]
            g.add_edge(n1, n2, capacity=1)

    _, flow_dict = nx.algorithms.flow.maximum_flow(g, source, sink)
    for rn in reviewers:
        for pn in papers:
            n1 = reviewer_nodes[rn]
            n2 = paper_nodes[pn]
            if flow_dict[n1][n2] > 0:
                yield (rn, pn)

if __name__ == '__main__':
    import sys, json

    datafile = sys.argv[1]

    with open(datafile) as f:
        data = json.load(f)
        reviewers = data['reviewers']
        papers = data['papers']
        conflicts = data['conflicts']

        results = build_graph(reviewers, papers, conflicts)

    for reviewer, paper in results:
        print('%s, %s' % (reviewer, paper))
