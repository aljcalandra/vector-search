import pinecone

with open('api-key') as f:
    pinecone.init(f.read(), environment='gcp-starter')

index = pinecone.Index('test')

# index.upsert([("a", [1.,1.]),("b", [2.,2.]),("c", [3.,3.])])

fetch_results = index.fetch(ids=["a", "b", "c"])
print(fetch_results)

query_results = index.query([1.1, 1.1], top_k=2)
print(query_results)

print(index.describe_index_stats())
