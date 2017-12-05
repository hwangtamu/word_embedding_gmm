from n_gram import Predictor

p = 'model/t8-2s-e10-v05-lr05d-mc100-ss5-nwout-adg-win10'
q = 'model/wiki1'
pred = Predictor(q)
#w2gm.visualize_embeddings()

a = 'hypr is a provider of real time analytics solution allowing brand owners to partner with social media influencers to promote their brands the platform provides influencer audience demographic psychographic and geographic data the company was founded in and is based in new york united states it has office in tel aviv israel hypr is an influencer marketing platform the farm provides clients audience demographics of social influencers it allows marketers to engage their target audience by hiring any number of influencers ranging from a single to thousands the platform allows automation in influencer discovery by narrowing down large number of options to relevant ones the company tracks over million influencers and billion social accounts daily the company was founded in gil eyal who is the current ceo of the company eyal is a known figure in the israeli startup scene he has a history of working with celebrities as the coo of photo sharing app mobli where he became a pioneer in the influencer marketing space for the app he recruited celebrities including leonardo dicaprio serena williams lil wayne and austin mahone the company claims to have a different algorithm from other marketing platform the engine of the platform crawls different social media accounts around the world and uses proprietary databases and algorithms to understand the nature of their audience demographics allowing the engine to make informed recommendation and find influencers that directly reach to the relevant audience in june hypr audience demographic and profile information as its feature the engine uses an index of million influencers across major social channels its client base includes fortune brands and pr and advertising agencies globally including lvmh hearst magazines calvin klein time inc and est e lauder'
# t = pred.get_neightbours('hypr', a)
# for i in t:
#     print(i, pred.model.get_dist(i))

print(pred.get_clusters('hypr', a))

