import spacy

# Read movie descriptions from movies.txt and store them in a list
def read_movie_descriptions():
    movie_descriptions = []
    with open("movies.txt", "r") as file:
        for line in file:
            movie_descriptions.append(line.strip())
    return movie_descriptions

# Load the spaCy language model (you can change the model to en_core_web_sm by replacing en_core_web_md)
nlp = spacy.load("en_core_web_md")

# Calculate similarity scores between the given description and all other movie descriptions
def calculate_similarity_scores(target_description, movie_descriptions):
    target_doc = nlp(target_description)
    similarity_scores = []
    for description in movie_descriptions:
        doc = nlp(description)
        similarity = target_doc.similarity(doc)
        similarity_scores.append(similarity)
    return similarity_scores

# Find the title of the most similar movie
def recommend_movie(target_description, movie_descriptions, movie_titles):

    target_doc = nlp(target_description)

    similarity_scores = calculate_similarity_scores(target_description, movie_descriptions)
    
    if not similarity_scores:
        return "No movies available."
    
    max_similarity_index = similarity_scores.index(max(similarity_scores))
    return movie_titles[max_similarity_index]

if __name__ == "__main__":
    movie_descriptions = read_movie_descriptions()
    

    movie_titles = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie F", "Movie G", "Movie H", "Movie I", "Movie J"]  # Replace with your movie titles
    
    if len(movie_descriptions) != len(movie_titles):
        print("Error: The number of movie descriptions and titles should match.")
    else:
        target_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
        
        target_doc = nlp(target_description)
        
        recommended_movie = recommend_movie(target_description, movie_descriptions, movie_titles)
        print(f"Recommended Movie: {recommended_movie}")
