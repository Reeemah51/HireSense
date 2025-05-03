data = [
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Which algorithm takes the data to the next dimension and then classify?",
        "answer": "Support Vector Machines (SVM), specifically with kernel tricks, take the data to a higher-dimensional space where the classes become more separable. This is useful when data is not linearly separable in its original space. SVM applies a kernel function, such as the Radial Basis Function (RBF), to map the data into higher dimensions, then finds the optimal hyperplane that separates the classes. This ability to map to higher dimensions allows SVM to classify non-linearly separable data effectively."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are categorical variables and what do we do with categorical variables?",
        "answer": "Categorical variables are variables that represent discrete categories or groups rather than continuous values. Examples include gender, color, or brand name. These variables often need to be converted into a numerical format for machine learning algorithms that require numerical input. The most common techniques for handling categorical variables are One-Hot Encoding, where each category is represented by a binary column, and Label Encoding, where each category is assigned a unique integer value. The choice of method depends on the type of model being used and the nature of the data."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What does it mean to have low MAE and high MSE?",
        "answer": "MAE (Mean Absolute Error) is the average of the absolute errors between predicted and actual values, while MSE (Mean Squared Error) is the average of the squared differences. Having low MAE and high MSE indicates that most of the predictions are close to the actual values (low MAE), but there are a few significant outliers (high MSE) that disproportionately affect the overall error. This suggests that the model has a few large errors that are causing the high MSE, even though the majority of predictions are relatively accurate."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the disadvantages of linear regression?",
        "answer": "Linear regression assumes a linear relationship between the independent and dependent variables, which may not hold in all cases, leading to inaccurate predictions. It is sensitive to outliers, which can significantly distort the results. It also assumes homoscedasticity (constant variance of errors), which might not always be the case in real-world data. Additionally, linear regression cannot handle multicollinearity well (when independent variables are highly correlated), and it assumes the errors are normally distributed, which may not always hold true."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is a recommendation engine? How does it work?",
        "answer": "A recommendation engine is a system that suggests products, services, or content to users based on their preferences or behavior. It works using one of two main methods: Collaborative filtering, which analyzes past user behavior to predict future preferences, and Content-based filtering, which suggests items similar to those the user has liked before. Hybrid models combine both methods for more accurate recommendations."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is K-means? How can you select K for K-means?",
        "answer": "K-means is a clustering algorithm that partitions data into K distinct groups based on the similarity of data points. The value of K represents the number of clusters the algorithm will generate. To select K, methods like the Elbow Method can be used, where you plot the sum of squared distances from each point to its assigned cluster center (within-cluster sum of squares) for different values of K. The 'elbow' point on the plot suggests the optimal K value, where increasing K further does not result in significant gains in clustering performance."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Does the Radial Basis Kernel function exist in SVM?",
        "answer": "Yes, the Radial Basis Function (RBF) kernel is commonly used in Support Vector Machines (SVM) for classification tasks. The RBF kernel maps the data into a higher-dimensional space, making it possible to find a hyperplane that separates non-linearly separable data in the original feature space. It works by calculating the similarity between data points based on a Gaussian function, where the points closer to each other in feature space are mapped into higher dimensions where they are separable."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is linear regression? Why is it called linear?",
        "answer": "Linear regression is a statistical model that assumes a linear relationship between the independent (predictor) variables and the dependent (response) variable. It is called 'linear' because the model estimates the best-fit line using the equation y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ, where the coefficients (β) are linearly related to the predictors, and the relationship between the variables is assumed to be linear."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Is pruning always a good method to construct a tree?",
        "answer": "Pruning is generally a good method to prevent overfitting in decision trees by removing nodes that provide little predictive power. However, pruning may not always be ideal, especially if the tree is already small or the data is very complex, where pruning could potentially remove important information. The decision to prune depends on the specific problem and the size of the dataset. In some cases, pruning can reduce model performance, so it's important to balance pruning with the need for model complexity."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the difference between bagging and boosting?",
        "answer": "Bagging (Bootstrap Aggregating) is an ensemble technique that trains multiple models independently on different subsets of the data and combines their predictions, usually through averaging (regression) or voting (classification). This reduces variance and improves model stability. Boosting, on the other hand, trains models sequentially, where each model tries to correct the errors made by the previous one. It focuses on high-error data points, thus reducing bias. Boosting tends to be more prone to overfitting than bagging, but often results in higher accuracy."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Which algorithm uses margin to classify the classes?",
        "answer": "Support Vector Machines (SVM) use the concept of margins to classify data. SVM finds the optimal hyperplane that maximizes the margin between the closest data points from each class (known as support vectors). This approach helps to ensure the best separation of the classes and provides a robust classifier, especially when the data is not linearly separable."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What algorithm can be used to summarize Twitter feed?",
        "answer": "A text summarization algorithm, such as Latent Dirichlet Allocation (LDA) for topic modeling or Extractive Summarization methods (e.g., using TF-IDF or neural networks like BERT), can be used to summarize a Twitter feed. These algorithms can identify key topics, entities, and important events within a large volume of tweets and provide a condensed summary based on frequency or importance."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How do you generate arbitrary or random shape clusters?",
        "answer": "To generate arbitrary or random-shaped clusters, DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is often used, as it does not require the clusters to be spherical. DBSCAN can identify clusters of varying shapes based on the density of points, and it is capable of detecting outliers. Another technique is Gaussian Mixture Models (GMM), which can model data as a combination of multiple Gaussian distributions, allowing for the generation of arbitrary cluster shapes."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How to compute the standard error of the median in a simple way?",
        "answer": "The standard error of the median can be approximated using bootstrapping, a statistical method that resamples the data with replacement to create multiple simulated samples. The standard deviation of the medians from these resampled datasets provides an estimate of the standard error of the median. Alternatively, you can use the jackknife method, which systematically leaves out one observation at a time to estimate variability."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How does GBDTs decide to split a node? What does it minimize?",
        "answer": "Gradient Boosting Decision Trees (GBDT) decide to split a node by selecting the feature and split point that minimizes a loss function, typically the mean squared error (MSE) for regression tasks or log loss for classification tasks. The decision to split is based on the gradient of the loss function, which guides the tree to focus on reducing prediction errors. The goal is to find the optimal splits that improve the model's accuracy by correcting errors in the previous models."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the difference between R-squared and Adjusted R-squared?",
        "answer": "R-squared (R²) represents the proportion of the variance in the dependent variable that is explained by the independent variables. However, it tends to increase as more predictors are added to the model, even if the new predictors do not contribute meaningfully. Adjusted R-squared adjusts for the number of predictors, providing a more accurate measure of model fit, especially when comparing models with different numbers of predictors. Adjusted R² can decrease if the added predictors do not improve the model."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How is matrix factorization useful in recommendation systems?",
        "answer": "Matrix factorization is a key technique used in collaborative filtering-based recommendation systems. It decomposes the user-item interaction matrix into two lower-dimensional matrices that capture latent factors (user preferences and item characteristics) responsible for predicting interactions. This technique helps reduce the sparsity of the matrix and can reveal hidden patterns, making it possible to recommend items to users based on these latent features. Singular Value Decomposition (SVD) is one of the most popular matrix factorization methods used in recommendation systems."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the approximation methods in Reinforcement Learning?",
        "answer": "In Reinforcement Learning, approximation methods are used to estimate value functions and policies when the state or action spaces are too large to handle with exact methods. Two common approximation methods are value function approximation, which approximates the state-value function (V(s)) or action-value function (Q(s, a)) using techniques like linear regression or neural networks, and policy approximation, where the policy is approximated by a function such as a neural network. Q-learning with function approximation and Deep Q-Networks (DQN) are popular methods in this category."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the difference between an error and a residual error?",
        "answer": "An error refers to the difference between an observed value and the true value of the parameter being estimated, while a residual error is the difference between an observed value and the predicted value from a model. In practice, residual errors are used for model evaluation, as the true values of parameters are rarely known, but residuals can provide insight into the model's accuracy."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why does training an SVM take a long time? How can I speed up?",
        "answer": "Training an SVM can be slow, particularly for large datasets, because it requires solving a quadratic optimization problem to find the optimal hyperplane. As the size of the dataset increases, the computational complexity grows exponentially. To speed up SVM training, you can use techniques like kernel approximation, linear SVMs for large datasets, and parallelization or stochastic gradient descent (SGD). Additionally, reducing the dimensionality of the data through PCA (Principal Component Analysis) can help reduce training time."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Difference between bagging, boosting, and the relation to Bayes' theorem?",
        "answer": "Bagging (Bootstrap Aggregating) reduces variance by training multiple models on different subsets of the data and combining their predictions. Boosting reduces bias by training models sequentially, where each subsequent model corrects the errors of the previous one. In contrast, Bayes' theorem is used to calculate probabilities based on prior knowledge and evidence. While Bayes' theorem is a foundational concept in probabilistic models, bagging and boosting are ensemble methods used to improve predictive performance by combining multiple weak models."
    },
        {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is padding?",
        "answer": "Padding is the process of adding extra values (usually zeros) to the input of a neural network, particularly in convolutional neural networks (CNNs), to ensure the output size is consistent and retains important spatial features. Padding is commonly used to preserve the dimensions of input data after applying convolution operations, especially when using small filter sizes. It helps avoid losing information at the edges of the image or sequence, ensuring that all input elements are processed."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Sigmoid vs Softmax",
        "answer": "Sigmoid is an activation function that maps input values to a range between 0 and 1, commonly used for binary classification tasks. It outputs probabilities for two classes. Softmax, on the other hand, is used in multi-class classification problems, where it converts a vector of raw scores (logits) into a probability distribution, with each output representing the likelihood of each class. Softmax ensures the probabilities across all classes sum to 1, whereas sigmoid outputs a separate probability for each class independently."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is PoS Tagging?",
        "answer": "PoS (Part-of-Speech) Tagging is the process of assigning a part of speech to each word in a sentence, such as noun, verb, adjective, etc. It is a crucial step in NLP tasks as it helps the model understand the grammatical structure of a sentence. For instance, in the sentence 'She runs quickly,' 'She' would be tagged as a pronoun, 'runs' as a verb, and 'quickly' as an adverb."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is tokenization?",
        "answer": "Tokenization is the process of splitting text into smaller units, called tokens, which can be words, phrases, or even characters. This is one of the first steps in NLP tasks, as it breaks down raw text into manageable chunks that can be analyzed and processed. For example, in the sentence 'I love AI,' tokenization would split it into the tokens ['I', 'love', 'AI']."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is topic modeling?",
        "answer": "Topic modeling is a technique used to automatically identify the underlying topics in a collection of text documents. It is an unsupervised learning method that groups words that frequently appear together in documents and associates them with specific topics. Common algorithms used for topic modeling include Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF). For instance, in a set of news articles, topic modeling might identify themes such as 'sports,' 'politics,' or 'technology.'"
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is back propagation?",
        "answer": "Backpropagation is a supervised learning algorithm used to train artificial neural networks. It involves calculating the gradient of the loss function with respect to each weight by applying the chain rule, and then adjusting the weights to minimize the loss. This process helps optimize the neural network by propagating errors from the output layer back to the input layer, updating weights at each layer along the way to reduce prediction error."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "What is the idea behind GANs?",
        "answer": "Generative Adversarial Networks (GANs) consist of two neural networks: a generator and a discriminator. The generator creates synthetic data (e.g., images), while the discriminator evaluates how realistic the data is. The goal is for the generator to fool the discriminator into classifying synthetic data as real. The two networks compete, and as training progresses, the generator produces increasingly realistic data. GANs are widely used for tasks like image generation, style transfer, and data augmentation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the computational graph?",
        "answer": "A computational graph is a directed graph where nodes represent operations (such as addition, multiplication, or other functions), and edges represent the flow of data between these operations. It is often used to describe and implement neural networks, where the graph captures the sequence of operations to perform on input data. The graph structure allows for efficient computation, especially in frameworks like TensorFlow and PyTorch, by enabling automatic differentiation and optimization of computations."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is sigmoid? What does it do?",
        "answer": "The sigmoid function is an activation function used in neural networks that maps input values to a range between 0 and 1. It is defined as sigmoid(x) = 1 / (1 + e^(-x)). Sigmoid is often used in binary classification tasks where the output is interpreted as a probability. However, it is not commonly used in hidden layers of deep networks due to its vanishing gradient problem, which makes it less effective for training deep networks."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is Named-Entity Recognition (NER)?",
        "answer": "Named-Entity Recognition (NER) is a subtask of information extraction that locates and classifies named entities in text into predefined categories, such as the names of persons, organizations, locations, dates, etc. For example, in the sentence 'Barack Obama was born in Hawaii on August 4, 1961,' an NER system would recognize 'Barack Obama' as a person, 'Hawaii' as a location, and 'August 4, 1961' as a date."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Explain the masked language model.",
        "answer": "A masked language model (MLM) is a type of language model where some portion of the input tokens is replaced with a mask token, and the model is trained to predict the missing words. This is the approach used in models like BERT (Bidirectional Encoder Representations from Transformers). The advantage of MLM is that it allows the model to learn contextual relationships between words in both directions (left-to-right and right-to-left), making it more effective at understanding the meaning of words in context."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How do you preprocess text in NLP?",
        "answer": "Text preprocessing in NLP typically involves several steps:\n\nTokenization: Splitting the text into smaller units (words or subwords).\nLowercasing: Converting all text to lowercase to ensure uniformity.\nRemoving stop words: Eliminating common words like 'the,' 'and,' etc., that don’t add much meaning.\nStemming or Lemmatization: Reducing words to their root forms.\nRemoving special characters or punctuation: Cleaning the text for analysis.\nVectorization: Converting the text into numerical representations (like TF-IDF, word2vec, or embeddings). These steps help prepare the text for machine learning algorithms."
    }, 
      {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How do you extract features in NLP?",
        "answer": "Feature extraction in NLP involves converting text data into numerical representations that machine learning models can process. Common techniques include:\n\n- Bag of Words (BoW): Represents text as a matrix where each word is counted and assigned a value.\n- TF-IDF (Term Frequency-Inverse Document Frequency): Weighs words based on their importance in a document relative to a corpus.\n- Word embeddings: Converts words into continuous vector representations using methods like word2vec, GloVe, or fastText. These embeddings capture semantic relationships between words.\n- N-grams: Captures the context of words by considering adjacent words or sequences.\n- Topic modeling: Identifies hidden topics in text by clustering words related to specific themes."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How is word2vec different from GloVe?",
        "answer": "word2vec and GloVe are both methods for creating word embeddings, but they differ in their approaches:\n\n- word2vec (Word2Vec) uses a shallow neural network model to predict the context of a word based on surrounding words (Skip-Gram or Continuous Bag of Words). It’s trained using the local context of words in a window, which captures semantic relationships.\n- GloVe (Global Vectors for Word Representation) is based on matrix factorization and constructs embeddings by capturing global word co-occurrence statistics from a corpus. It combines the benefits of global matrix factorization and local context, aiming to capture global relationships between words in a text corpus."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the different layers in CNN?",
        "answer": "In a Convolutional Neural Network (CNN), the layers are organized as follows:\n\n- Convolutional Layer: Applies filters to the input to detect features like edges, textures, and patterns.\n- Activation Layer (ReLU): Adds non-linearity to the model, allowing it to learn complex patterns.\n- Pooling Layer (Max Pooling or Average Pooling): Reduces the spatial dimensions (height and width) to decrease computational load and prevent overfitting.\n- Fully Connected Layer: Connects each neuron in one layer to every neuron in the next, typically found before the output layer.\n- Output Layer: Produces the final prediction (for classification, regression, etc.)."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What makes CNNs translation invariant?",
        "answer": "Translation invariance in CNNs is achieved through the use of pooling layers. In CNNs, pooling operations like max pooling and average pooling reduce the spatial size of the feature maps. This helps the network become less sensitive to small translations or shifts in the input image, allowing it to recognize objects regardless of their position in the image."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How is fastText different from word2vec?",
        "answer": "fastText and word2vec are both methods for generating word embeddings, but fastText improves upon word2vec by considering subword information. In word2vec, each word is treated as a single unit, while fastText breaks words into character n-grams (subwords). This allows fastText to create better embeddings for rare words or out-of-vocabulary words by using their subword representations, making it more robust in handling morphologically rich languages."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "Explain Generative Adversarial Network (GAN).",
        "answer": "A Generative Adversarial Network (GAN) consists of two neural networks: a generator and a discriminator. The generator creates synthetic data (e.g., images), while the discriminator evaluates whether the data is real or fake. The two networks are trained in opposition: the generator tries to fool the discriminator into classifying fake data as real, and the discriminator tries to correctly identify real vs. fake data. Over time, this adversarial process results in the generator producing highly realistic data. GANs are widely used for image generation, data augmentation, and style transfer."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is backward and forward propagation?",
        "answer": "Forward Propagation is the process where input data passes through the network, layer by layer, to compute the output. In each layer, the weighted sum of inputs is calculated, and an activation function is applied. This output is used to make predictions.\nBackward Propagation (backpropagation) is the process of updating the network’s weights by calculating the gradient of the loss function with respect to each weight, using the chain rule of calculus. This is done to minimize the error between the predicted output and the true value. The weights are adjusted to reduce the loss during training."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "What are Syntactic and Semantic Analysis?",
        "answer": "Syntactic Analysis (syntax parsing) is the process of analyzing the structure of a sentence based on grammar rules, breaking it down into its components like subjects, predicates, and objects. The goal is to determine the syntactic structure, which is important for understanding sentence structure.\nSemantic Analysis focuses on understanding the meaning of words and phrases in context. It aims to understand the relationships between words and their meanings, allowing for better comprehension of sentences beyond just grammar."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is a local optimum?",
        "answer": "A local optimum is a solution to an optimization problem that is better than its neighboring solutions, but not necessarily the best overall solution (which would be a global optimum). In many machine learning algorithms, local optima can be a challenge as they may lead the algorithm to settle for a suboptimal solution, especially when the objective function is non-convex."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "Explain gates used in LSTM with their functions.",
        "answer": "Long Short-Term Memory (LSTM) networks use three primary gates to control the flow of information:\n\n- Forget Gate: Decides which information from the previous hidden state should be discarded or 'forgotten.' It outputs values between 0 and 1, where 1 means 'keep' and 0 means 'forget.'\n- Input Gate: Determines which new information should be stored in the cell state. It controls the update of the cell state and incorporates information from the current input and the previous hidden state.\n- Output Gate: Decides what information should be output from the LSTM cell. It controls the next hidden state and determines which part of the cell state should be passed to the next layer."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is ReLU? How is it better than sigmoid or tanh?",
        "answer": "ReLU (Rectified Linear Unit) is an activation function that outputs the input directly if it’s positive; otherwise, it outputs zero. Mathematically, ReLU(x) = max(0, x). ReLU is widely used in deep neural networks because it is computationally efficient and helps mitigate the vanishing gradient problem, unlike sigmoid or tanh, which suffer from saturating gradients. ReLU allows faster learning and is less likely to lead to gradient-related issues during backpropagation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is transfer learning? Have you used it before?",
        "answer": "Transfer Learning is a machine learning technique where a pre-trained model is used on a new task, allowing the model to leverage knowledge learned from one problem to solve another, often related problem. This is particularly useful when there is limited data available for the new task. In practice, I have used transfer learning in image classification tasks, where I fine-tuned a pre-trained ResNet model on a new dataset of images. This significantly improved model performance, reducing the time and computational cost required to train from scratch."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is multi-task learning? When should it be used?",
        "answer": "Multi-task Learning (MTL) is a learning paradigm where a model is trained to perform multiple tasks simultaneously, leveraging shared representations to improve performance across all tasks. MTL is useful when tasks are related, and sharing information between them helps improve learning efficiency and generalization. For example, in NLP, a model could simultaneously perform sentiment analysis and named-entity recognition (NER) tasks, where shared features between the tasks help improve overall model performance."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Difference between convex and non-convex cost function?",
        "answer": "A convex cost function is one where the line segment between any two points on the function lies above the function itself, meaning it has a single global minimum. Convex functions are easier to optimize since gradient-based methods are guaranteed to converge to the global minimum.\nIn contrast, a non-convex cost function may have multiple local minima, making optimization more challenging, as gradient-based methods may get stuck in a local minimum instead of the global minimum. Many machine learning problems, such as training deep neural networks, involve non-convex cost functions."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why do we remove stop words? When do we not remove them?",
        "answer": "Stop words are common words like 'and,' 'the,' 'is,' 'in,' and 'on' that are often removed during text preprocessing in NLP tasks, as they do not carry significant meaning and are typically deemed irrelevant for analysis. Removing stop words helps reduce dimensionality and improves computational efficiency.\nHowever, stop words may not be removed in cases where the task involves understanding sentence structure or context, such as in sentiment analysis or machine translation. In these tasks, the presence of stop words might be important for retaining the meaning of the sentence."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Explain the difference between an epoch, a batch, and an iteration.",
        "answer": "Epoch: One complete pass through the entire training dataset. If the dataset has 1,000 samples, one epoch means the model has seen all 1,000 samples once.\nBatch: A subset of the training dataset used to train the model. During training, the dataset is divided into smaller batches to update the model's weights iteratively.\nIteration: The number of batches processed in one epoch. For example, if the dataset has 1,000 samples and the batch size is 100, then it would take 10 iterations to complete one epoch."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the difference between NLP and NLU?",
        "answer": "Natural Language Processing (NLP) refers to the broader field of AI and computational linguistics focused on enabling machines to understand, interpret, and generate human language. It involves tasks like text classification, tokenization, machine translation, and named entity recognition.\nNatural Language Understanding (NLU), on the other hand, is a subfield of NLP that focuses specifically on machine comprehension of human language. It deals with understanding the meaning behind the text, such as sentiment analysis, intent recognition, and context extraction. NLU is often seen as the more advanced subset of NLP, as it involves deeper comprehension and interpretation of language."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Give a simple mathematical argument why a mini-batch version of such ML algorithm might be computationally more efficient than training with a full data set.",
        "answer": "Mini-batch gradient descent is computationally more efficient than using the full dataset because it strikes a balance between the noisy updates from stochastic gradient descent (SGD) and the computationally expensive full-batch gradient descent. By using smaller batches, we reduce the computation cost per update, making the process faster. Mathematically, mini-batch updates allow the algorithm to move towards convergence more quickly by utilizing the parallel computation of smaller data subsets, which also reduces memory requirements compared to using the entire dataset."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "On a simplified and fundamental scale, what makes the newly developed BERT model better than traditional NLP models?",
        "answer": "BERT (Bidirectional Encoder Representations from Transformers) improves on traditional NLP models by utilizing a bidirectional attention mechanism, meaning it looks at both the left and right context of a word simultaneously, as opposed to earlier models that only considered context from one direction. This allows BERT to better understand the nuanced meanings of words in different contexts. Additionally, BERT is pre-trained on large amounts of text data, enabling it to learn general language patterns before fine-tuning for specific tasks, making it highly efficient and powerful in a wide range of NLP applications."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How would you initialize weights in a neural network?",
        "answer": "To initialize weights in a neural network, it's common to use small random values to break symmetry between neurons. For example, one popular method is Xavier initialization, which scales the weights based on the number of input and output units of each layer. This helps avoid issues where neurons might learn the same features or have vanishing/exploding gradients. Another option is He initialization, which is designed to work well with ReLU activation functions by scaling the weights by a factor of 2 divided by the number of input units."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why are weights initialized with small random numbers in a neural network? What happens when weights are all or constant values?",
        "answer": "Weights are initialized with small random values to break symmetry and allow neurons to learn different features. If weights are all initialized to the same value (such as zero), every neuron would receive the same gradient during backpropagation, leading to identical updates and preventing the network from learning diverse features. Random initialization ensures that each neuron begins with a unique starting point, allowing the network to learn effectively and efficiently."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Suppose you have a neural network with layers and ReLU activations. What will happen if we initialize all the weights with the same value?",
        "answer": "If all weights in a neural network with ReLU activations are initialized to the same value, the network will suffer from a symmetry problem. During backpropagation, all neurons will receive the same gradients and learn the same features, effectively making each neuron redundant. As a result, the network will fail to capture the diversity of features needed for effective learning. It's crucial to initialize the weights with different values to ensure that each neuron learns a unique representation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is backpropagation? How does it work, and why do we need it?",
        "answer": "Backpropagation is a supervised learning algorithm used to train neural networks. It calculates the gradients of the loss function with respect to the network's weights by applying the chain rule of calculus. Starting from the output layer, the error is propagated backward through the network, adjusting the weights to minimize the loss. Backpropagation is essential because it enables efficient weight updates, allowing the network to learn patterns in the data and improve its performance over time."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why can large filter sizes in early layers be a bad choice? How to choose filter size?",
        "answer": "Large filter sizes in early layers can be a bad choice because they result in fewer feature maps and a loss of fine-grained spatial information. Early layers should capture low-level features like edges, which require smaller filters (e.g., 3x3 or 5x5). Larger filters in the first layers can blur out important details. Typically, smaller filters are preferred in early layers to capture detailed features, and larger filters are used in deeper layers to capture more abstract patterns."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Which one is more powerful: a single-layer decision tree or a multi-layer neural network without any activation function? Hint: non-linearity",
        "answer": "A multi-layer neural network without any activation function would essentially behave like a linear model, as non-linearity is crucial for learning complex patterns. A single-layer decision tree, however, is inherently capable of making non-linear splits in the data based on feature thresholds. Thus, in terms of non-linearity, the decision tree has the advantage as it can capture non-linear relationships between features. However, a multi-layer neural network with activation functions would be much more powerful, as it introduces non-linearity, enabling the network to model more complex relationships."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Both decision trees and deep neural networks are non-linear classifiers (i.e., they separate the space by a complicated decision boundary). Why is it so much easier for us to intuitively follow a decision tree model vs. a deep neural network?",
        "answer": "Decision trees are more intuitive because their decision-making process is hierarchical and transparent. We can follow the splits based on feature thresholds and understand why a particular decision was made. Each branch of the tree represents a simple rule that is easy to interpret. On the other hand, deep neural networks are black-box models with many layers and complex transformations, making it much harder for humans to trace how the model arrived at a decision. The lack of transparency in neural networks makes them more difficult to interpret, which is why decision trees are often preferred for explainability."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "If you could take advantage of multiple CPU cores, would you prefer a boosted-tree algorithm over a random forest?",
        "answer": "Yes, if I could take advantage of multiple CPU cores, I would prefer using boosted-tree algorithms (like XGBoost or LightGBM) over a random forest in many cases. Boosted trees typically outperform random forests, especially on structured/tabular data. While both algorithms use decision trees, boosting builds trees sequentially, where each new tree corrects the errors of the previous one, leading to higher accuracy. Random forests, on the other hand, build trees independently and combine them through averaging. Boosted trees generally yield better performance at the cost of longer training time, but with multi-core processing, the training time can be reduced significantly."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Describe two ways to visualize features of a CNN in an image classification task.",
        "answer": "Filter Visualization: In CNNs, each convolutional layer has a set of filters (or kernels) that learn to detect various features such as edges, textures, or colors. Visualizing these filters can help understand what kind of patterns each filter is looking for. For example, the first layer might learn simple features like horizontal or vertical edges, while deeper layers might capture more complex patterns.\n\nActivation Map Visualization: After applying a filter to an image, the resulting activation map shows which parts of the image are most influential in making a prediction. By visualizing these activations, we can see which areas of the image the network focuses on during classification, providing insights into its decision-making process."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why do segmentation CNNs typically have an encoder-decoder style/structure?",
        "answer": "Segmentation tasks require pixel-wise classification, where each pixel in the image must be assigned a label. The encoder-decoder structure is used in segmentation CNNs to first downsample the image and learn the high-level features in the encoder part, followed by the decoder part that upscales the feature maps back to the original image size for precise pixel-wise predictions. This architecture helps the model maintain both spatial context and fine details needed for accurate segmentation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is a convolutional layer? Why do we actually need convolutions? Can we use fully-connected layers for that?",
        "answer": "A convolutional layer applies a set of filters (kernels) to the input image, performing element-wise multiplication and summing the results to produce feature maps. This allows the network to automatically learn spatial hierarchies in the data, such as edges, textures, and more complex patterns as it deepens. We need convolutions because they preserve the spatial structure of the input, whereas fully-connected layers treat every input as independent, losing spatial relationships. Using fully-connected layers for this purpose would require significantly more parameters and fail to capture local dependencies in image data effectively."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the advantages of parameter sharing in the case of convolution?",
        "answer": "Parameter sharing in convolutional layers means that the same filter is applied across different parts of the input image. This reduces the number of parameters significantly, making the network more computationally efficient and less prone to overfitting. It also allows the network to learn translation-invariant features, meaning the network can recognize the same pattern regardless of where it appears in the image. This is a key advantage in image processing tasks, where spatial relationships are important."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why do we use convolutions for images rather than just fully-connected layers?",
        "answer": "We use convolutions for images because they are efficient in capturing local patterns and spatial hierarchies, such as edges, textures, and shapes. Convolutional layers allow us to apply the same filter across the image, reducing the number of parameters and preserving spatial relationships. In contrast, fully-connected layers treat each pixel independently and do not retain spatial relationships, making them computationally expensive and less effective for image processing tasks."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why would you use many small convolutional kernels, such as 3x3, rather than a few large ones?",
        "answer": "Using many small convolutional kernels, like 3x3, instead of a few large ones is beneficial because smaller kernels allow the network to learn more fine-grained features and build up complex patterns through deeper layers. For example, using multiple 3x3 filters is equivalent to using one large filter (like 7x7) but with fewer parameters, enabling the model to capture more detailed information. Additionally, smaller filters lead to better generalization, reduced computational cost, and a more modular approach to feature learning."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why do we generally use the Softmax non-linearity function as the last operation in a network?",
        "answer": "We use Softmax at the output layer, particularly in classification tasks, because it converts the raw output scores of the network into a probability distribution. It ensures that the sum of the output probabilities equals 1, which is ideal for tasks where we need to predict the likelihood of each class. Softmax helps interpret the model’s outputs in terms of probabilities, making the decision process more interpretable and useful for classification."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How does Batch Normalization differ in training and inferencing?",
        "answer": "Batch Normalization (BN) normalizes the activations of the network during training by adjusting them to have a mean of zero and variance of one, improving convergence speed and stability. During training, BN uses the statistics of each mini-batch to normalize the activations. During inference, however, BN uses the running averages of the mean and variance (calculated during training) to normalize activations, ensuring consistency across different inputs. This helps avoid discrepancies between training and inference."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How does batch size affect the training of neural networks?",
        "answer": "The batch size impacts the training dynamics of neural networks. Smaller batch sizes lead to more noisy updates, which can help the model escape local minima but might result in slower convergence. Larger batch sizes provide more stable gradients but can slow down the training process and require more memory. Typically, a batch size is chosen based on available hardware, the model's complexity, and the desired balance between convergence speed and stability. Smaller batches are often preferred for larger datasets."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "When using mini-batch gradient descent, why is it important to shuffle the data?",
        "answer": "Shuffling the data when using mini-batch gradient descent is crucial to avoid the model learning in a biased way. If the data is not shuffled, the algorithm might learn patterns from the data sequence, leading to poor generalization. Shuffling ensures that each mini-batch represents a random subset of the data, allowing the model to train more effectively and converge to a better solution. It also helps prevent cycles or overfitting, making the learning process more robust."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How do you get sentence meanings from word embeddings, considering the position of words in the sentence?",
        "answer": "To get sentence meanings from word embeddings, we typically use methods like averaging the word embeddings of all words in a sentence, or more sophisticated approaches like Word2Vec, GloVe, or BERT, which consider the context of words in sentences. Positioning can be captured by using positional encodings in transformer models, which helps the model differentiate word order. The combination of word embeddings and positional information gives a rich representation of sentence meaning, capturing both the meaning of individual words and their relationships to one another."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Would you prefer gradient boosting trees model or logistic regression when doing text classification with bag of words?",
        "answer": "For text classification with a bag of words, I would generally prefer gradient boosting trees (e.g., XGBoost or LightGBM) over logistic regression for most scenarios. This is because gradient boosting methods handle non-linearity better, are more robust to overfitting, and often provide better performance on complex datasets, which is common in text classification. Logistic regression, while simpler and interpretable, may struggle when relationships in the data are more complex. However, if interpretability and simplicity are key, logistic regression could still be a viable choice."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is bag of words? How can we use it for text vectorization?",
        "answer": "Bag of Words (BoW) is a text vectorization technique that represents text data as a set of words (or tokens) and their frequencies within a document, without considering the order of the words. This method creates a matrix where each row corresponds to a document, and each column corresponds to a unique word in the corpus. The matrix cells hold the word counts (or term frequency) of each word in a document. BoW is simple and effective but loses semantic information and word order."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the advantages and disadvantages of bag of words?",
        "answer": "Advantages of BoW:\n\n- Simplicity: Easy to understand and implement.\n- Interpretability: The resulting vectors are sparse and easy to work with.\n- Effective for simple tasks: Works well in many basic text classification tasks, such as spam detection.\n\nDisadvantages of BoW:\n\n- Loss of context: Ignores word order, meaning, and relationships between words.\n- High dimensionality: The feature space can grow very large, especially with large vocabularies, leading to sparse matrices.\n- No handling of synonyms: Different words with similar meanings are treated as separate features."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the main difference between Adam and SGD?",
        "answer": "Adam (Adaptive Moment Estimation) is an optimization algorithm that combines the benefits of AdaGrad and RMSProp. It adapts the learning rate for each parameter by considering both the first and second moments (mean and variance) of the gradients. This makes Adam more efficient in dealing with sparse gradients and noisy data.\n\nSGD (Stochastic Gradient Descent), on the other hand, updates the parameters using the gradient of the loss function, computed from a single data point or a small batch. It is simpler and often works well, but can be slower and less effective on complex or sparse datasets due to the constant learning rate."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the advantages and disadvantages of SGD over gradient descent?",
        "answer": "Advantages of SGD:\n\n- Faster updates: Since it updates the parameters with each data point, it converges faster in many cases, especially for large datasets.\n- Less memory intensive: Unlike batch gradient descent, which requires storing the entire dataset in memory, SGD only needs a single data point at a time.\n- Better at escaping local minima: Due to its noisy updates, SGD has a better chance of avoiding getting stuck in local minima.\n\nDisadvantages of SGD:\n\n- Noisy updates: Can lead to high variance and instability in the optimization process.\n- May take longer to converge: While faster in the initial stages, SGD might require more iterations to converge compared to batch methods, especially for very complex models."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "What is the difference between stochastic gradient descent (SGD) and gradient descent (GD), batch gradient descent, stochastic gradient descent, mini-batch gradient descent, and what are the pros and cons for each of them?",
        "answer": "Batch Gradient Descent (GD) computes the gradient of the entire dataset for each update, leading to precise updates but with high computational cost, especially with large datasets. It’s slow and doesn’t work well for big data.\n\nStochastic Gradient Descent (SGD) updates parameters after processing each individual data point, making it faster but more noisy. It’s efficient for large datasets but can be unstable and might not converge as smoothly.\n\nMini-batch Gradient Descent is a compromise, using a small subset (mini-batch) of data to compute the gradient, which speeds up training and reduces the variance compared to SGD while being more computationally efficient than batch gradient descent. It is the most commonly used in practice.\n\nPros and Cons:\n\n- Batch GD: Precise but computationally expensive.\n- SGD: Fast and memory efficient but noisy and potentially unstable.\n- Mini-batch GD: Balanced, good for large datasets and tends to converge faster than full batch methods."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "When would you use GD over SGD and vice-versa?",
        "answer": "You would use Gradient Descent (GD) when you have a small dataset that fits into memory and you want precise, stable updates. It works well for convex problems or situations where an exact solution is needed.\n\nStochastic Gradient Descent (SGD) is preferred when you have a large dataset, as it can process one data point at a time, making it faster and more memory efficient. It is commonly used in deep learning models, especially when training on large-scale datasets where speed is essential."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How would you choose the number of filters and the filter size at each CNN layer?",
        "answer": "The number of filters in each CNN layer depends on the complexity of the task and the dataset. Generally, we start with fewer filters in the earlier layers (e.g., 32 or 64) and increase the number as we go deeper into the network. This allows the network to capture increasingly complex features at higher levels of abstraction.\n\nAs for the filter size, a typical choice is 3x3 filters, as they are small enough to capture fine details and computationally efficient. Larger filters like 5x5 or 7x7 are used when more spatial context is needed. A good strategy is to experiment with different sizes and numbers based on the task’s complexity."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How can we use CNN for text classification?",
        "answer": "To use CNN for text classification, we treat the text as a sequence of words or characters and apply 1D convolutional layers to extract local features from the text. Each filter in the convolution layer learns to detect patterns like specific word combinations or n-grams. These learned features are then pooled and passed to fully connected layers for classification. CNNs are effective in text classification because they can capture hierarchical features in the text, much like they do for images, and are particularly useful for tasks like sentiment analysis and document categorization."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are some advantages in using a CNN (Convolutional Neural Network) rather than a DNN (Dense Neural Network) in an image classification task?",
        "answer": "The key advantage of using CNNs over DNNs in image classification is that CNNs are designed to take advantage of the spatial hierarchy in images. They use convolutional layers to detect local patterns (like edges or textures), pooling layers to reduce dimensionality, and fully connected layers to make predictions. This makes CNNs highly efficient at processing images, as they require fewer parameters compared to fully connected networks, reducing the computational load.\n\nOn the other hand, DNNs typically treat each pixel as a separate feature, losing spatial relationships between pixels, which results in a less efficient and less accurate model for image classification tasks."
    },
     {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why is Rectified Linear Unit a good activation function?",
        "answer": "ReLU is a good activation function because it introduces non-linearity while being computationally efficient. It outputs the input directly if positive, and zero otherwise, which allows the model to learn complex patterns. Unlike sigmoid or tanh, ReLU avoids the vanishing gradient problem, making it faster to train and helping deep networks learn more effectively. Additionally, it is easy to implement and reduces the likelihood of the gradient getting stuck in small values during backpropagation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why don't we use the ReLU activation function in the output layer?",
        "answer": "We typically don’t use ReLU in the output layer because its range is from 0 to infinity, which is not ideal for tasks like classification where we need outputs within a specific range. For binary classification, we often use a Sigmoid activation (range 0 to 1), and for multi-class classification, we use Softmax (range 0 to 1, summing to 1). These activation functions ensure that the output can be interpreted as probabilities, which isn’t the case with ReLU."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What can go wrong if we use a linear activation instead of ReLU?",
        "answer": "Using a linear activation function instead of ReLU can limit the network's ability to model complex non-linear relationships. A linear activation function doesn’t introduce any non-linearity into the network, so the entire neural network essentially becomes a linear regressor, regardless of how many layers we add. This means the network will fail to capture the complex patterns necessary for tasks like image classification or language modeling, where non-linearity is crucial for learning from the data."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Give examples in which a many-to-one RNN architecture is appropriate.",
        "answer": "A many-to-one RNN architecture is appropriate in tasks where we have sequential input data but only need a single output. For example:\n\n- Sentiment analysis: An RNN processes a sequence of words (sentence) and outputs a single sentiment value (positive/negative).\n- Time series forecasting: A sequence of past observations is used to predict a single future value. In both cases, the RNN processes the sequence and compresses it into a single representation to make the final prediction."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is RNN and How does an RNN work?",
        "answer": "An RNN (Recurrent Neural Network) is a type of neural network designed for processing sequences of data. Unlike traditional feedforward networks, RNNs have loops in their architecture, allowing information to be passed from one time step to the next. This gives them memory, which makes them suitable for tasks involving sequential or time-dependent data. RNNs maintain hidden states that update as new inputs come in, allowing them to remember past information while making predictions based on the sequence seen so far."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why are Sigmoid or Tanh not preferred to be used as the activation function in the hidden layer of the neural network?",
        "answer": "Sigmoid and Tanh are not preferred for hidden layers because they suffer from the vanishing gradient problem. Both functions squash their output into a small range, causing gradients to shrink during backpropagation. This can result in very slow training or no training at all, especially in deep networks. ReLU, on the other hand, is preferred because it does not saturate for positive input values, allowing for faster convergence during training."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Difference between various activation functions such as Sigmoid, Tanh, Softmax, ReLU, Leaky ReLU.",
        "answer": "Sigmoid: Outputs values between 0 and 1, commonly used in binary classification but suffers from vanishing gradients.\nTanh: Outputs values between -1 and 1, used in hidden layers, but also suffers from vanishing gradients.\nSoftmax: Used in the output layer for multi-class classification; it converts the raw output into a probability distribution.\nReLU: Outputs zero for negative inputs and the input itself for positive inputs, popular for hidden layers due to its simplicity and efficiency.\nLeaky ReLU: A variant of ReLU where small negative values are allowed for negative inputs, helping to avoid dead neurons and improving learning."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why is the Tanh activation function preferred over Sigmoid?",
        "answer": "Tanh is preferred over Sigmoid because it has a wider output range of -1 to 1, making it zero-centered, which can help prevent the problem of shifting gradients. The Sigmoid function outputs values between 0 and 1, which can cause issues when training deep networks because the gradients can become too small and slow down learning. Tanh's zero-centered output makes it easier for the network to learn and converge faster."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are word embeddings? Why are they useful?",
        "answer": "Word embeddings are dense vector representations of words, where each word is mapped to a vector in a continuous vector space. They capture semantic relationships between words, meaning similar words are represented by vectors that are close to each other in this space. Word embeddings are useful because they reduce the dimensionality of the data compared to one-hot encoding and help capture the meaning of words based on their context, making them essential for tasks like sentiment analysis, machine translation, and information retrieval."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is WordVec?",
        "answer": "WordVec refers to the Word2Vec algorithm, which is a method for learning word embeddings from large corpora. It uses two main models: the Continuous Bag of Words (CBOW) model and the Skip-Gram model. Word2Vec transforms words into continuous vectors where similar words are closer together. It’s commonly used in NLP tasks because it captures the semantic meaning of words in a way that one-hot encoding cannot."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are some advantages of using character embeddings instead of word embeddings?",
        "answer": "Character embeddings have a few advantages over word embeddings:\n\n- Handling Out-of-Vocabulary Words: Character-level embeddings can represent any word, even those not seen during training, because they are based on the individual characters.\n- Morphological Flexibility: They can capture word variations such as tense, number, and other morphological changes that word embeddings might struggle with.\n- More Fine-Grained Representation: Character embeddings can be more precise in capturing subword information, which is useful for languages with complex morphology or for handling typos and misspellings."
    },
     {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What happens to the predictions of a CNN if an image is rotated?",
        "answer": "In a traditional Convolutional Neural Network (CNN), the predictions may be less accurate if an image is rotated, as CNNs are not inherently invariant to rotation. However, CNNs can still detect features in different orientations, but the model may not perform well unless it is trained with various rotated images. To overcome this limitation, techniques like data augmentation, where the training dataset includes rotated versions of the images, can help the model become more robust to such transformations."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How does CNN help in translation and rotation invariance of images?",
        "answer": "CNNs help achieve translation invariance through their use of pooling layers. Pooling reduces the spatial resolution of feature maps, which makes the model less sensitive to small translations of the image. However, CNNs are not inherently rotation-invariant. To achieve rotation invariance, techniques like data augmentation (rotating images during training), or using more advanced networks like Spatial Transformer Networks (STNs), can improve the model's ability to recognize objects regardless of their orientation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Define Term Frequency & Inverse Document Frequency (Tf-idf) and how to use it for converting text to a vector.",
        "answer": "Tf-idf is a numerical statistic used to represent text data. Term Frequency (TF) measures how often a word appears in a document relative to all other words. Inverse Document Frequency (IDF) measures how important a word is across the entire corpus, giving more weight to rare words. Tf-idf is calculated by multiplying TF by IDF for each word, and it can be used to convert text data into vectors where each word is represented by its tf-idf score. This vector representation is useful for various NLP tasks like text classification and document clustering."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the three primary convolutional neural network layers? How are they commonly put together?",
        "answer": "The three primary layers in a CNN are:\n\n- Convolutional layer: This layer applies filters to the input image to extract features like edges and textures. It performs a convolution operation between the image and filter.\n- Pooling layer: This layer reduces the spatial dimensions (height and width) of the feature maps, retaining important features while reducing computational complexity.\n- Fully connected layer: After feature extraction and pooling, the fully connected layer classifies the image by connecting the extracted features to the output classes.\n\nThese layers are typically stacked together in a hierarchical fashion, starting with convolutional layers followed by pooling layers, and ending with fully connected layers for final classification."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Describe the architecture of a typical Convolutional Neural Network.",
        "answer": "A typical CNN consists of several stages:\n\n- Input layer: The image is input into the network, usually as a 3D tensor representing height, width, and color channels.\n- Convolutional layers: These layers apply various filters to the image to extract features such as edges, corners, and textures.\n- Activation functions: After convolution, an activation function (typically ReLU) is applied to introduce non-linearity into the model.\n- Pooling layers: These reduce the dimensionality of the feature maps and make the network more invariant to transformations like scaling and translation.\n- Fully connected layers: After feature extraction, the flattened feature maps are passed through fully connected layers for classification or regression tasks.\n- Output layer: This layer produces the final predictions, usually through a softmax function for multi-class classification."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What do you mean by Dropout and Batch Normalization, When and why use?",
        "answer": "Dropout is a regularization technique used during training to prevent overfitting. It works by randomly setting a percentage of neuron activations to zero during each training iteration, forcing the network to learn more robust features.\n\nBatch Normalization is a technique used to normalize the inputs to each layer during training, which helps in stabilizing learning and accelerating training. It ensures that the inputs to the network are within a certain range, reducing the risk of vanishing or exploding gradients.\n\nBoth methods are used to improve the model's generalization ability and prevent overfitting, especially in deep neural networks."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the difference between online and batch learning?",
        "answer": "Online learning refers to a model training method where the model is updated continuously as new data arrives, allowing the model to learn incrementally. It’s useful in real-time systems or when the data is too large to be processed all at once.\n\nBatch learning involves training a model on the entire dataset at once, where the model is trained on fixed batches of data and updated only after processing each batch. It works well for static datasets but can be less efficient for real-time applications."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Is dropout used on the test set?",
        "answer": "No, dropout is only used during training. During the test phase, all the neurons are used to make predictions. The dropout mechanism is turned off to allow the full model capacity to evaluate the test data. This ensures that the model is evaluated in its optimal state."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is an activation function and discuss the use of an activation function?",
        "answer": "An activation function is a mathematical operation applied to the output of a neural network node (neuron) to introduce non-linearity. Without activation functions, the network would essentially be a linear regressor, unable to model complex patterns. Common activation functions include ReLU (Rectified Linear Unit), Sigmoid, and Tanh, each serving a different purpose, such as introducing non-linearity or constraining output values."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Explain three different types of activation functions.",
        "answer": "ReLU (Rectified Linear Unit): The most commonly used activation function, ReLU outputs zero for negative inputs and the input itself for positive inputs. It helps solve the vanishing gradient problem and allows models to train faster.\n\nSigmoid: Outputs values between 0 and 1, making it useful for binary classification. However, it suffers from the vanishing gradient problem when values are close to 0 or 1.\n\nTanh (Hyperbolic Tangent): Similar to the sigmoid, but it outputs values between -1 and 1. It is zero-centered, which often makes it a better choice than sigmoid for hidden layers."
    },
      {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How to select a batch size? Will selecting a batch size produce better or worse results?",
        "answer": "The batch size is crucial for balancing computation speed and model accuracy. A small batch size can lead to more noise during training, possibly resulting in better generalization, but it also increases the variance of the gradients. A large batch size leads to more stable gradients but might overfit. The optimal size depends on the dataset and the model architecture. I prefer experimenting with different sizes to see what works best for the task at hand."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are N-grams? How can we use them?",
        "answer": "N-grams are contiguous sequences of 'n' words from a given text or speech sample. For example, in the sentence 'AI is amazing,' the 2-grams would be 'AI is' and 'is amazing.' They are used in NLP tasks like language modeling, text classification, and machine translation to understand word patterns and context."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How large should N be for our bag of words when using N-grams?",
        "answer": "The value of N in N-grams typically ranges from 1 to 5. Smaller values like 1 (unigrams) capture individual words, while larger values capture more context. The choice depends on the task and computational constraints. A common approach is to try different values and evaluate the model’s performance."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "High",
        "question": "How can you use neural nets for text classification and computer vision?",
        "answer": "For text classification, I would use architectures like CNNs or RNNs (e.g., LSTMs), which can capture word patterns or sequences. For computer vision, CNNs are commonly used to learn spatial hierarchies in images, performing tasks like object detection or image classification. Both applications rely on neural nets to automatically extract relevant features from the raw data."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "High",
        "question": "Do gradient descent methods always converge at the same point?",
        "answer": "No, gradient descent methods may not always converge at the same point. This is because the starting point and the learning rate can significantly affect the convergence. In non-convex functions, it may converge to different local minima or saddle points depending on initialization and other factors like batch size or momentum."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is gradient descent? How does it work?",
        "answer": "Gradient descent is an optimization algorithm used to minimize the loss function in machine learning. It works by iteratively updating the model’s parameters in the direction of the steepest decrease in the loss (negative gradient). The learning rate controls the step size during each update."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "High",
        "question": "What are autoencoders? Explain the different layers of autoencoders and mention three practical usages of them.",
        "answer": "Autoencoders are unsupervised neural networks used for dimensionality reduction or feature learning. They consist of an encoder, which compresses the input into a lower-dimensional representation, and a decoder, which reconstructs the input from this representation. Practical uses include noise reduction, anomaly detection, and image compression."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is vanishing gradient descent?",
        "answer": "Vanishing gradient descent occurs when gradients become very small during backpropagation, making it hard for the network to learn. This issue is common in deep networks with activation functions like sigmoid or tanh, which squash values into a small range. It prevents weight updates and hampers learning."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Difference between vanishing gradient and exploding gradient?",
        "answer": "Vanishing gradients occur when the gradients become too small, slowing learning. Exploding gradients, on the other hand, happen when the gradients grow too large, causing model instability. Both issues arise during backpropagation, but they need different techniques to address: vanishing gradients can be mitigated with activation functions like ReLU, while exploding gradients can be addressed by gradient clipping."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How to handle dying node problems in the case of the ReLU activation function?",
        "answer": "The 'dying ReLU' problem occurs when neurons output zero for all inputs, making them inactive during training. To mitigate this, we can use variations of ReLU like Leaky ReLU or Parametric ReLU, which allow small negative gradients when the unit is inactive, helping the neurons to recover and learn."
    },
     {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "For online learning, which one would you prefer: SGD or Adagrad and why?",
        "answer": "If I had to choose between SGD (Stochastic Gradient Descent) and Adagrad for online learning, I would prefer SGD for its simplicity and effectiveness in handling large datasets. SGD is computationally more efficient, especially in real-time learning environments, because it updates the model incrementally with each new data point. Adagrad, on the other hand, adapts the learning rate based on the gradients, which works well for sparse datasets but tends to shrink the learning rate too quickly over time, especially on dense data. For most online learning applications where the dataset is constantly evolving, SGD offers more stability and flexibility."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What Is a Multi-layer Perceptron (MLP)?",
        "answer": "A Multi-layer Perceptron (MLP) is a type of artificial neural network that consists of multiple layers of nodes, or neurons, where each node is connected to every other node in adjacent layers. It is a fully connected feedforward neural network, meaning the data moves in one direction, from input to output, without any feedback loops. The network typically has an input layer that receives data, one or more hidden layers where computations are done, and an output layer that produces the final result. MLPs are powerful for tasks like classification and regression as they can model complex non-linear relationships in data."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Is it always bad to have local optima?",
        "answer": "Not always. While local optima can be problematic in certain optimization tasks, particularly in complex models where we want to reach the global optimum, they aren't always detrimental. In some cases, local optima can still provide solutions that are good enough for the problem at hand. For instance, in certain large-scale machine learning problems, reaching a local optimum may be sufficient to create a model that performs well and generalizes effectively. In practice, many algorithms, like simulated annealing or genetic algorithms, are designed to escape local optima and explore the solution space more effectively."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "In node2vec, what does embedding represent: topological similarity or nearness?",
        "answer": "In node2vec, the embedding represents topological similarity, or more specifically, structural proximity between nodes in a graph. The node2vec algorithm uses a biased random walk to capture the relationships between nodes, focusing on both local and global structures. The goal is to learn a low-dimensional representation of each node such that the distance between embeddings reflects how similar or close the nodes are in terms of their network position. So, the embedding captures both topological similarity and nearness in a graph, allowing us to understand how nodes are related structurally."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "What do you understand by Boltzmann Machine and Restricted Boltzmann Machines?",
        "answer": "A Boltzmann Machine (BM) is an unsupervised probabilistic recurrent neural network designed to learn the probability distribution over its set of visible and hidden units. It is called a Markov Random Field, and it uses a system of stochastic binary units to model complex relationships in data. However, BMs can be slow to train and computationally expensive because of their fully connected structure.\n\nA Restricted Boltzmann Machine (RBM) is a simplified version of a Boltzmann Machine where there are no intra-layer connections between the visible or hidden layers, only between the visible and hidden layers. This restriction makes training much more efficient and allows for fast training of deep models like deep belief networks (DBNs). The RBM is widely used for feature extraction, dimensionality reduction, and as a pretraining step for deeper networks."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How to compute an inverse matrix faster by playing around with some computational tricks?",
        "answer": "To compute an inverse matrix faster, several tricks and optimizations can be applied:\n\n- LU Decomposition: Decomposing a matrix into its lower (L) and upper (U) triangular matrices can make it more efficient to compute the inverse. Once decomposed, the inverse of the original matrix can be found much more easily.\n- Matrix Inversion Lemma: If you already have an inverse for part of a matrix, and only small updates are needed, Sherman-Morrison or Woodbury formulas can be used to update the inverse without recalculating from scratch.\n- Block Matrix Inversion: If your matrix has a block structure (like diagonal or block diagonal matrices), you can use the properties of these blocks to speed up the inversion.\n- Preconditioning: This involves transforming the matrix into a form where the condition number is better suited for inversion, speeding up numerical solvers.\n\nBy using these techniques, matrix inversion can be made faster, especially for large matrices or those with special structures."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "For infrequent or rare words, which among CBOW and SkipGram should be used for word2vec training?",
        "answer": "For infrequent or rare words, the Skip-gram model is generally more effective. Here's why:\n\nSkip-gram focuses on predicting context words given a target word, which works well for rare words because it allows the model to learn from the surrounding context even if the rare word itself doesn't appear often in the dataset.\nCBOW (Continuous Bag of Words), on the other hand, is better suited for more frequent words, as it predicts the target word from the context, and it might struggle with rare words due to a lack of sufficient training data.\nTherefore, Skip-gram is typically the better choice when dealing with rare words since it is designed to give more weight to the context, which helps in learning good embeddings for infrequent terms."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is pooling in CNN? Why do we need it?",
        "answer": "In Convolutional Neural Networks (CNNs), pooling is a downsampling operation that reduces the spatial dimensions of the input feature map. This helps decrease the computational complexity and the number of parameters, which can reduce the risk of overfitting. The two common types of pooling are:\n\n- Max pooling: Selects the maximum value from each patch of the feature map (usually 2x2 or 3x3).\n- Average pooling: Averages the values in the patch.\n\nWhy do we need pooling?\n\n- Reduces Computational Load: Pooling reduces the dimensionality of feature maps, making the model faster and less computationally expensive.\n- Prevents Overfitting: By reducing the spatial size, pooling helps the model generalize better and reduces the risk of overfitting.\n- Translation Invariance: Pooling introduces a slight invariance to translations, meaning the model can recognize objects even if they are slightly shifted in position within the image."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Describe the structure of Artificial Neural Networks (ANN) & RNN (Recurrent Neural Network).",
        "answer": "Artificial Neural Networks (ANN):\n\n- Input layer: Receives the input data (features).\n- Hidden layers: Layers between the input and output where data is processed using weighted sums and activation functions (like ReLU or Sigmoid).\n- Output layer: Produces the final output of the network (such as classification or regression predictions).\n\nEach neuron in a hidden layer is connected to every neuron in adjacent layers, which makes ANN a fully connected network. ANNs are used in many supervised learning tasks such as classification and regression.\n\nRecurrent Neural Networks (RNN):\n\n- RNNs are designed for sequence data (e.g., text, speech, time series). The key difference from ANNs is that RNNs have feedback loops in the network, allowing them to retain information across time steps.\n- Input layer: Like ANNs, it receives the input sequence.\n- Recurrent layers: These layers process data sequentially, passing information from one time step to the next via loops, which allows RNNs to capture temporal dependencies in the data.\n- Output layer: Produces the final output, which could be for tasks like sequence generation, classification, or time series forecasting.\n\nRNNs are particularly suited for sequential data tasks like language modeling, speech recognition, and time series forecasting, where the order and context of inputs matter."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Why do we remove stop words? When do we not remove them?",
        "answer": "Stop words are common words like 'and,' 'the,' 'is,' 'in,' and 'on' that are often removed during text preprocessing in NLP tasks, as they do not carry significant meaning and are typically deemed irrelevant for analysis. Removing stop words helps reduce dimensionality and improves computational efficiency.\n\nHowever, stop words may not be removed in cases where the task involves understanding sentence structure or context, such as in sentiment analysis or machine translation. In these tasks, the presence of stop words might be important for retaining the meaning of the sentence."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Explain the difference between an epoch, a batch, and an iteration.",
        "answer": "Epoch: One complete pass through the entire training dataset. If the dataset has 1,000 samples, one epoch means the model has seen all 1,000 samples once.\nBatch: A subset of the training dataset used to train the model. During training, the dataset is divided into smaller batches to update the model's weights iteratively.\nIteration: The number of batches processed in one epoch. For example, if the dataset has 1,000 samples and the batch size is 100, then it would take 10 iterations to complete one epoch."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the difference between NLP and NLU?",
        "answer": "Natural Language Processing (NLP) refers to the broader field of AI and computational linguistics focused on enabling machines to understand, interpret, and generate human language. It involves tasks like text classification, tokenization, machine translation, and named entity recognition.\n\nNatural Language Understanding (NLU), on the other hand, is a subfield of NLP that focuses specifically on machine comprehension of human language. It deals with understanding the meaning behind the text, such as sentiment analysis, intent recognition, and context extraction. NLU is often seen as the more advanced subset of NLP, as it involves deeper comprehension and interpretation of language."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How do you extract features in NLP?",
        "answer": "Feature extraction in NLP involves converting text data into numerical representations that machine learning models can process. Common techniques include:\n\n- Bag of Words (BoW): Represents text as a matrix where each word is counted and assigned a value.\n- TF-IDF (Term Frequency-Inverse Document Frequency): Weighs words based on their importance in a document relative to a corpus.\n- Word embeddings: Converts words into continuous vector representations using methods like word2vec, GloVe, or fastText. These embeddings capture semantic relationships between words.\n- N-grams: Captures the context of words by considering adjacent words or sequences.\n- Topic modeling: Identifies hidden topics in text by clustering words related to specific themes."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How is word2vec different from GloVe?",
        "answer": "word2vec and GloVe are both methods for creating word embeddings, but they differ in their approaches:\n\n- word2vec (Word2Vec) uses a shallow neural network model to predict the context of a word based on surrounding words (Skip-Gram or Continuous Bag of Words). It’s trained using the local context of words in a window, which captures semantic relationships.\n- GloVe (Global Vectors for Word Representation) is based on matrix factorization and constructs embeddings by capturing global word co-occurrence statistics from a corpus. It combines the benefits of global matrix factorization and local context, aiming to capture global relationships between words in a text corpus."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What are the different layers in CNN?",
        "answer": "In a Convolutional Neural Network (CNN), the layers are organized as follows:\n\n- Convolutional Layer: Applies filters to the input to detect features like edges, textures, and patterns.\n- Activation Layer (ReLU): Adds non-linearity to the model, allowing it to learn complex patterns.\n- Pooling Layer (Max Pooling or Average Pooling): Reduces the spatial dimensions (height and width) to decrease computational load and prevent overfitting.\n- Fully Connected Layer: Connects each neuron in one layer to every neuron in the next, typically found before the output layer.\n- Output Layer: Produces the final prediction (for classification, regression, etc.)."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What makes CNNs translation invariant?",
        "answer": "Translation invariance in CNNs is achieved through the use of pooling layers. In CNNs, pooling operations like max pooling and average pooling reduce the spatial size of the feature maps. This helps the network become less sensitive to small translations or shifts in the input image, allowing it to recognize objects regardless of their position in the image."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How is fastText different from word2vec?",
        "answer": "fastText and word2vec are both methods for generating word embeddings, but fastText improves upon word2vec by considering subword information. In word2vec, each word is treated as a single unit, while fastText breaks words into character n-grams (subwords). This allows fastText to create better embeddings for rare words or out-of-vocabulary words by using their subword representations, making it more robust in handling morphologically rich languages."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "Explain Generative Adversarial Network (GAN).",
        "answer": "A Generative Adversarial Network (GAN) consists of two neural networks: a generator and a discriminator. The generator creates synthetic data (e.g., images), while the discriminator evaluates whether the data is real or fake. The two networks are trained in opposition: the generator tries to fool the discriminator into classifying fake data as real, and the discriminator tries to correctly identify real vs. fake data. Over time, this adversarial process results in the generator producing highly realistic data. GANs are widely used for image generation, data augmentation, and style transfer."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is backward and forward propagation?",
        "answer": "Forward Propagation is the process where input data passes through the network, layer by layer, to compute the output. In each layer, the weighted sum of inputs is calculated, and an activation function is applied. This output is used to make predictions.\n\nBackward Propagation (backpropagation) is the process of updating the network’s weights by calculating the gradient of the loss function with respect to each weight, using the chain rule of calculus. This is done to minimize the error between the predicted output and the true value. The weights are adjusted to reduce the loss during training."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "What are Syntactic and Semantic Analysis?",
        "answer": "Syntactic Analysis (syntax parsing) is the process of analyzing the structure of a sentence based on grammar rules, breaking it down into its components like subjects, predicates, and objects. The goal is to determine the syntactic structure, which is important for understanding sentence structure.\n\nSemantic Analysis focuses on understanding the meaning of words and phrases in context. It aims to understand the relationships between words and their meanings, allowing for better comprehension of sentences beyond just grammar."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is a local optimum?",
        "answer": "A local optimum is a solution to an optimization problem that is better than its neighboring solutions, but not necessarily the best overall solution (which would be a global optimum). In many machine learning algorithms, local optima can be a challenge as they may lead the algorithm to settle for a suboptimal solution, especially when the objective function is non-convex."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "Explain gates used in LSTM with their functions.",
        "answer": "Long Short-Term Memory (LSTM) networks use three primary gates to control the flow of information:\n\n- Forget Gate: Decides which information from the previous hidden state should be discarded or 'forgotten.' It outputs values between 0 and 1, where 1 means 'keep' and 0 means 'forget.'\n- Input Gate: Determines which new information should be stored in the cell state. It controls the update of the cell state and incorporates information from the current input and the previous hidden state.\n- Output Gate: Decides what information should be output from the LSTM cell. It controls the next hidden state and determines which part of the cell state should be passed to the next layer."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is ReLU? How is it better than sigmoid or tanh?",
        "answer": "ReLU (Rectified Linear Unit) is an activation function that outputs the input directly if it’s positive; otherwise, it outputs zero. Mathematically, $ReLU(x) = max(0, x)$. ReLU is widely used in deep neural networks because it is computationally efficient and helps mitigate the vanishing gradient problem, unlike sigmoid or tanh, which suffer from saturating gradients. ReLU allows faster learning and is less likely to lead to gradient-related issues during backpropagation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is transfer learning? Have you used it before?",
        "answer": "Transfer Learning is a machine learning technique where a pre-trained model is used on a new task, allowing the model to leverage knowledge learned from one problem to solve another, often related problem. This is particularly useful when there is limited data available for the new task. In practice, I have used transfer learning in image classification tasks, where I fine-tuned a pre-trained ResNet model on a new dataset of images. This significantly improved model performance, reducing the time and computational cost required to train from scratch."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is multi-task learning? When should it be used?",
        "answer": "Multi-task Learning (MTL) is a learning paradigm where a model is trained to perform multiple tasks simultaneously, leveraging shared representations to improve performance across all tasks. MTL is useful when tasks are related, and sharing information between them helps improve learning efficiency and generalization. For example, in NLP, a model could simultaneously perform sentiment analysis and named-entity recognition (NER) tasks, where shared features between the tasks help improve overall model performance."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Difference between convex and non-convex cost function?",
        "answer": "A convex cost function is one where the line segment between any two points on the function lies above the function itself, meaning it has a single global minimum. Convex functions are easier to optimize since gradient-based methods are guaranteed to converge to the global minimum.\nIn contrast, a non-convex cost function may have multiple local minima, making optimization more challenging, as gradient-based methods may get stuck in a local minimum instead of the global minimum. Many machine learning problems, such as training deep neural networks, involve non-convex cost functions."
    },
     {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is padding?",
        "answer": "Padding is the process of adding extra values (usually zeros) to the input of a neural network, particularly in convolutional neural networks (CNNs), to ensure the output size is consistent and retains important spatial features. Padding is commonly used to preserve the dimensions of input data after applying convolution operations, especially when using small filter sizes. It helps avoid losing information at the edges of the image or sequence, ensuring that all input elements are processed."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Sigmoid vs Softmax",
        "answer": "Sigmoid is an activation function that maps input values to a range between 0 and 1, commonly used for binary classification tasks. It outputs probabilities for two classes. Softmax, on the other hand, is used in multi-class classification problems, where it converts a vector of raw scores (logits) into a probability distribution, with each output representing the likelihood of each class. Softmax ensures the probabilities across all classes sum to 1, whereas sigmoid outputs a separate probability for each class independently."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is PoS Tagging?",
        "answer": "PoS (Part-of-Speech) Tagging is the process of assigning a part of speech to each word in a sentence, such as noun, verb, adjective, etc. It is a crucial step in NLP tasks as it helps the model understand the grammatical structure of a sentence. For instance, in the sentence 'She runs quickly,' 'She' would be tagged as a pronoun, 'runs' as a verb, and 'quickly' as an adverb."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is tokenization?",
        "answer": "Tokenization is the process of splitting text into smaller units, called tokens, which can be words, phrases, or even characters. This is one of the first steps in NLP tasks, as it breaks down raw text into manageable chunks that can be analyzed and processed. For example, in the sentence 'I love AI,' tokenization would split it into the tokens ['I', 'love', 'AI']."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is topic modeling?",
        "answer": "Topic modeling is a technique used to automatically identify the underlying topics in a collection of text documents. It is an unsupervised learning method that groups words that frequently appear together in documents and associates them with specific topics. Common algorithms used for topic modeling include Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF). For instance, in a set of news articles, topic modeling might identify themes such as 'sports,' 'politics,' or 'technology.'"
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is back propagation?",
        "answer": "Backpropagation is a supervised learning algorithm used to train artificial neural networks. It involves calculating the gradient of the loss function with respect to each weight by applying the chain rule, and then adjusting the weights to minimize the loss. This process helps optimize the neural network by propagating errors from the output layer back to the input layer, updating weights at each layer along the way to reduce prediction error."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Hard",
        "question": "What is the idea behind GANs?",
        "answer": "Generative Adversarial Networks (GANs) consist of two neural networks: a generator and a discriminator. The generator creates synthetic data (e.g., images), while the discriminator evaluates how realistic the data is. The goal is for the generator to fool the discriminator into classifying synthetic data as real. The two networks compete, and as training progresses, the generator produces increasingly realistic data. GANs are widely used for tasks like image generation, style transfer, and data augmentation."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is the computational graph?",
        "answer": "A computational graph is a directed graph where nodes represent operations (such as addition, multiplication, or other functions), and edges represent the flow of data between these operations. It is often used to describe and implement neural networks, where the graph captures the sequence of operations to perform on input data. The graph structure allows for efficient computation, especially in frameworks like TensorFlow and PyTorch, by enabling automatic differentiation and optimization of computations."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is sigmoid? What does it do?",
        "answer": "The sigmoid function is an activation function used in neural networks that maps input values to a range between 0 and 1. It is defined as $sigmoid(x) = \\frac{1}{1 + e^{-x}}$. Sigmoid is often used in binary classification tasks where the output is interpreted as a probability. However, it is not commonly used in hidden layers of deep networks due to its vanishing gradient problem, which makes it less effective for training deep networks."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "What is Named-Entity Recognition (NER)?",
        "answer": "Named-Entity Recognition (NER) is a subtask of information extraction that locates and classifies named entities in text into predefined categories, such as the names of persons, organizations, locations, dates, etc. For example, in the sentence 'Barack Obama was born in Hawaii on August 4, 1961,' an NER system would recognize 'Barack Obama' as a person, 'Hawaii' as a location, and 'August 4, 1961' as a date."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "Explain the masked language model.",
        "answer": "A masked language model (MLM) is a type of language model where some portion of the input tokens is replaced with a mask token, and the model is trained to predict the missing words. This is the approach used in models like BERT (Bidirectional Encoder Representations from Transformers). The advantage of MLM is that it allows the model to learn contextual relationships between words in both directions (left-to-right and right-to-left), making it more effective at understanding the meaning of words in context."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Intelligence",
        "difficulty": "Medium",
        "question": "How do you preprocess text in NLP?",
        "answer": "Text preprocessing in NLP typically involves several steps:\n\n- Tokenization: Splitting the text into smaller units (words or subwords).\n- Lowercasing: Converting all text to lowercase to ensure uniformity.\n- Removing stop words: Eliminating common words like 'the,' 'and,' etc., that don’t add much meaning.\n- Stemming or Lemmatization: Reducing words to their root forms.\n- Removing special characters or punctuation: Cleaning the text for analysis.\n- Vectorization: Converting the text into numerical representations (like TF-IDF, word2vec, or embeddings). These steps help prepare the text for machine learning algorithms."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "Explain Artificial Intelligence and give its applications.",
        "answer": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines, allowing them to perform tasks that typically require human-like cognition such as decision-making, problem-solving, and understanding natural language. Common applications of AI include image and speech recognition, natural language processing (NLP), self-driving cars, and recommendation systems. AI is also applied in healthcare for diagnostics, in finance for fraud detection, and in customer service through chatbots."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "How are machine learning and AI related?",
        "answer": "Machine learning (ML) is a subset of Artificial Intelligence (AI). While AI is the broader concept that includes any technique enabling machines to mimic human behavior, ML specifically focuses on algorithms that allow computers to learn patterns from data and improve over time without being explicitly programmed. Essentially, all machine learning is AI, but not all AI involves machine learning. AI also includes other techniques like rule-based systems and expert systems, which don't involve learning from data."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is Deep Learning based on?",
        "answer": "Deep learning is based on artificial neural networks, particularly those with multiple layers, known as deep neural networks (DNNs). These networks are inspired by the human brain's structure and are capable of learning from large amounts of data by processing it through various layers, each extracting more complex features. Deep learning excels at handling complex data like images, audio, and text due to its ability to automatically learn high-level representations."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "How many layers are in a Neural Network?",
        "answer": "A basic neural network typically has three layers: the input layer (which receives the data), one or more hidden layers (where the data is processed), and the output layer (which produces the final result or prediction). The number of hidden layers can vary depending on the complexity of the network; deeper networks (with more hidden layers) are used in more complex tasks like image recognition or natural language processing."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "Explain TensorFlow.",
        "answer": "TensorFlow is an open-source software library developed by Google for machine learning and artificial intelligence tasks, particularly deep learning. It provides a flexible and efficient platform for building and deploying machine learning models, especially neural networks. TensorFlow allows developers to easily create models, run them on various platforms (e.g., CPUs, GPUs, and TPUs), and optimize the model's performance through its powerful computational graph structure."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What are the pros of cognitive computing?",
        "answer": "Cognitive computing refers to systems that simulate human thought processes to solve complex problems. The pros of cognitive computing include its ability to process large volumes of data, adapt and learn from experiences, provide contextually relevant insights, and assist in decision-making by mimicking human cognitive functions. It can significantly enhance operational efficiency, improve customer interaction, and enable smarter decision-making in industries like healthcare, finance, and customer service."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What’s the difference between NLP and NLU?",
        "answer": "Natural Language Processing (NLP) is the broader field that enables computers to understand and process human language, including tasks like text generation, translation, and sentiment analysis. NLP covers a wide range of linguistic tasks, from syntax analysis to text classification. Natural Language Understanding (NLU) is a subfield of NLP focused specifically on understanding the meaning of text. NLU involves tasks such as named-entity recognition, intent detection, and semantic parsing, aiming to grasp context and intent beyond just the structure of the language."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "Give some examples of weak and strong AI.",
        "answer": "Weak AI, also known as narrow AI, is designed to perform specific tasks but lacks general intelligence. Examples include voice assistants like Siri, recommendation systems, or autonomous vehicles, which excel at one task but cannot perform general human-like tasks. Strong AI, or Artificial General Intelligence (AGI), refers to systems that can perform any intellectual task that a human can. Strong AI does not yet exist, but it would be able to reason, learn, and solve problems across multiple domains without task-specific programming."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is the need for data mining?",
        "answer": "Data mining is the process of discovering patterns, correlations, and useful insights from large datasets. It is essential for extracting actionable knowledge from massive amounts of raw data, enabling businesses to make informed decisions. The need for data mining arises because of the exponential growth in data generation and storage, making it impossible to manually analyze all the data. Data mining techniques, such as clustering, classification, and association rule learning, help uncover trends in industries like finance, healthcare, and marketing."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "Name some sectors where data mining is applicable.",
        "answer": "Data mining is widely used in sectors like:\n\n- Healthcare: For predicting patient outcomes, identifying fraudulent claims, and improving treatment strategies.\n- Finance: To detect fraud, assess credit risk, and predict stock prices.\n- Retail: For customer behavior analysis, sales forecasting, and inventory management.\n- Telecommunications: To optimize networks and detect fraud.\n- Marketing: To understand customer preferences and improve targeting strategies.\n- Manufacturing: For predictive maintenance and quality control.\nEach of these sectors uses data mining to derive meaningful insights and improve operational efficiency."
    },
     {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What are the components of NLP?",
        "answer": "There are three main components to NLP:\n\n- Language understanding: Interprets the meaning of the text.\n- Language generation: Produces text that is grammatically correct and conveys the intended meaning.\n- Language processing: Performs operations on text, such as tokenization, lemmatization, and part-of-speech tagging."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is the full form of LSTM?",
        "answer": "LSTM stands for Long Short-Term Memory, a type of recurrent neural network (RNN) architecture designed to handle long-range dependencies in sequential data, making it effective for tasks like speech recognition, language translation, and time series analysis."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is Artificial Narrow Intelligence (ANI)?",
        "answer": "Artificial Narrow Intelligence (ANI), also known as Weak AI, refers to AI systems designed to perform specific tasks with high efficiency but without general intelligence. These systems are highly specialized and excel at solving narrowly defined problems, like facial recognition or recommendation engines."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is a data cube?",
        "answer": "A data cube is a multidimensional representation of data, commonly used in data mining and analytics. It allows for the visualization of complex data in a 3D space, enabling quick analysis across multiple dimensions (e.g., time, location, and product type). This format helps in identifying patterns, trends, and correlations in large datasets."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is the difference between model accuracy and model performance?",
        "answer": "Model accuracy refers to the proportion of correct predictions made by the model compared to the total number of predictions. Model performance, on the other hand, is a broader term that includes various metrics like precision, recall, F1-score, AUC, and more. Performance metrics are typically more comprehensive in evaluating a model's overall effectiveness, especially in imbalanced datasets."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What are different components of GAN?",
        "answer": "A Generative Adversarial Network (GAN) consists of two main components:\n\n- Generator: A neural network that generates fake data (e.g., images) based on random noise.\n- Discriminator: A neural network that distinguishes between real and fake data. The generator and discriminator work together, with the generator improving to fool the discriminator, while the discriminator gets better at identifying fakes. This adversarial process helps in generating realistic data."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What are common data structures used in deep learning?",
        "answer": "Some common data structures in deep learning are:\n\n- Tensors: Multi-dimensional arrays that form the backbone of data representation in deep learning.\n- Matrices: Two-dimensional arrays, often used in operations like matrix multiplication.\n- Vectors: One-dimensional arrays, used to represent individual data points or model parameters.\nThese structures help in organizing and manipulating data for training neural networks."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is the role of the hidden layer in a neural network?",
        "answer": "The hidden layer in a neural network processes the input data by applying weights and activation functions. It transforms the input into a format that is more useful for the output layer, allowing the network to learn complex patterns and relationships in the data. The more hidden layers a network has, the deeper and more capable it is at modeling complex data."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "Mention some advantages of neural networks.",
        "answer": "Neural networks offer several advantages:\n\n- Ability to detect non-linear relationships: They excel at identifying complex patterns in data.\n- Adaptability: They can handle large datasets and adjust to new data.\n- Noise tolerance: Neural networks can filter out noise and focus on relevant features.\n- Continuous learning: They can adapt to changing input data by updating their weights.\nThese qualities make neural networks effective for tasks like image recognition, speech recognition, and NLP."
    },
    {
        "category": "Technology",
        "specialty": "Artificial Engineering",
        "difficulty": "Medium",
        "question": "What is the difference between stemming and lemmatization?",
        "answer": "Stemming is a process that removes suffixes from words to reduce them to a base form (e.g., 'running' to 'run'), while lemmatization involves reducing a word to its dictionary form (lemma) based on its context (e.g., 'better' to 'good'). Stemming is faster but less accurate, while lemmatization is more accurate but computationally more expensive."
    },
      {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Why do we need activation functions in neural networks?",
    "answer": "Activation functions play a vital role in neural networks, serving as a non-linear transformation applied to the output of a neuron or node. They determine the output of a neuron based on the weighted sum of its inputs, introducing non-linearity into the network. This non-linearity allows neural networks to model complex, non-linear relationships in the data."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Explain gradient descent.",
    "answer": "Gradient descent is a popular optimization algorithm used to find the minimum of a function iteratively. It is widely used in machine learning and deep learning for training models by minimizing the error or loss function, which measures the difference between the predicted and actual values."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is the purpose of data normalization?",
    "answer": "Data normalization is a pre-processing technique used to standardize and scale the features in a dataset. Its main purposes include improving model performance, ensuring fair comparisons by bringing features to a common scale, speeding up convergence in gradient-based optimization, and reducing numerical issues such as over- or underflow."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Name some activation functions.",
    "answer": "Common activation functions include sigmoid, tanh, and ReLU. The sigmoid function maps inputs to values between 0 and 1, tanh maps inputs to values between -1 and 1 providing a zero-centered output, and ReLU outputs 0 for negative inputs and the input itself for positive values, helping alleviate the vanishing gradient problem."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Briefly explain data augmentation.",
    "answer": "Data augmentation is a technique used to increase the amount of training data by creating modified versions of existing data. This is particularly important in deep learning, where large amounts of data are required to effectively train models."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What is the Swish function?",
    "answer": "The Swish function is an activation function that is smooth, non-linear, and differentiable. It has been shown to outperform some traditional activation functions like ReLU in certain deep learning tasks."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Explain forward propagation and backpropagation.",
    "answer": "Forward propagation is the process of computing the output of a neural network by passing the input through each layer and applying transformations using weights, biases, and activation functions. Backpropagation, on the other hand, involves computing the gradient of the loss function with respect to each weight and bias, which is then used to update these parameters using an optimization algorithm like gradient descent."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is classification and its benefits?",
    "answer": "Classification is a supervised learning task where the goal is to assign input data points to one of several predefined categories or labels. Benefits of classification include enabling informed decision-making, recognizing complex patterns, detecting anomalies, and personalizing recommendations or content based on learned patterns."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What is a convolutional neural network?",
    "answer": "A convolutional neural network (CNN) is a type of neural network particularly well-suited for image classification tasks. CNNs use convolutional layers to extract features from the input data, allowing the model to classify images into predefined categories. They are also applied in tasks like object recognition, sentiment analysis, and spam filtering."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Explain autoencoders and its types.",
    "answer": "Autoencoders are neural networks used for dimensionality reduction by learning a compressed representation of the input data. The main types include: Denoising Autoencoders, which reconstruct clean input from corrupted data; Sparse Autoencoders, which apply a sparsity constraint on hidden layers to prevent overfitting; and Undercomplete Autoencoders, which compress data without additional regularization as they naturally maximize data probability rather than simply copying input to output."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Explain Sentimental analysis in NLP?",
    "answer": "Sentiment analysis is the process of analyzing text to determine its emotional tone. This technique is widely used in customer service to understand how customers feel, and in social media to gauge public sentiment about a topic."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is BFS and DFS algorithm?",
    "answer": "Breadth-First Search (BFS) and Depth-First Search (DFS) are graph traversal algorithms. BFS starts at the root node (or any selected node) and visits all nodes at the current level before moving to the next level. In contrast, DFS starts at the root and explores as far as possible along each branch before backtracking."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Explain the difference between supervised and unsupervised learning.",
    "answer": "Supervised learning involves training a model on labeled data, where both input features and output labels are provided, allowing the model to learn the relationship and make predictions. Unsupervised learning, on the other hand, uses unlabeled data to discover hidden structures or patterns, such as clusters, in the data."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is the text extraction process?",
    "answer": "Text extraction is the process of retrieving text from sources such as images or documents. This can be done using Optical Character Recognition (OCR) or by converting the text into a format that can be read and processed by a text-to-speech system."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What are some disadvantages of linear models?",
    "answer": "Disadvantages of linear models include potential bias if the training data isn't representative of real-world conditions, the risk of overfitting when using a small dataset, and the assumption of a linear relationship between input features and the output, which may not hold true in complex scenarios."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Mention methods for reducing dimensionality.",
    "answer": "Reducing dimensionality involves decreasing the number of random variables under consideration. Methods to achieve this include Principal Component Analysis (PCA), low variance filtering, evaluating missing values ratio, high correlation filtering, and techniques using random forests, among others."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Explain cost function.",
    "answer": "A cost function is a scalar function that measures how far off a neural network's predictions are from the actual values. It quantifies the error in the model, and during training, the goal is to minimize this cost to improve the model's accuracy."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Mention hyper-parameters of ANN.",
    "answer": "Key hyper-parameters of an Artificial Neural Network (ANN) include: Learning rate (the speed at which the model learns), Momentum (helps escape local minima and smooths gradient descent), Number of epochs (how many times the training dataset is processed), Number of hidden layers, Number of neurons in each hidden layer, and the choice of activation functions such as Sigmoid, ReLU, or Tanh."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Explain intermediate tensors. Do sessions have a lifetime?",
    "answer": "Intermediate tensors are temporary data structures in a computational graph that store the results of operations during the forward pass in a neural network. In frameworks like TensorFlow 1.x, sessions manage these computations and have a defined lifetime starting from when they are created until they are closed. TensorFlow 2.x, however, uses eager execution which eliminates the explicit use of sessions."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Explain Exploding variables.",
    "answer": "Exploding variables refer to the rapid and uncontrolled growth in the magnitude of variables during training, often due to repeated multiplication by large factors. This leads to numerical instability and can result in overflow errors, severely hindering the training process of neural networks."
  },
   {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Is it possible to build a deep learning model only using linear regression?",
    "answer": "Linear regression is a basic tool in statistical learning, but it cannot be used to build a deep learning model. Deep learning models require non-linear functions to learn complex patterns in data."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is the function of Hyperparameters?",
    "answer": "Hyperparameters are parameters that are not learned by the model. They are set by the user and are used to control the model's behavior."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What is Artificial Super Intelligence (ASI)?",
    "answer": "Artificial Super Intelligence (ASI) is a hypothetical system that can surpass human intelligence and perform tasks better than a human. It has not been achieved yet and is envisioned to be capable of making complex decisions and developing nuanced, even emotional, relationships."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What is overfitting, and how can it be prevented in an AI model?",
    "answer": "Overfitting occurs when a model learns the training data too well, including noise and random fluctuations, resulting in poor performance on unseen data. Techniques to prevent overfitting include regularization (L1 or L2), early stopping, cross-validation, using more training data, and reducing model complexity."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is the role of pipeline for Information extraction (IE) in NLP?",
    "answer": "Pipelines in information extraction are used to sequentially apply a series of processing steps to input data, enabling efficient data processing and reducing errors."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What is the difference between full listing hypothesis and minimum redundancy hypothesis?",
    "answer": "The full listing hypothesis states that all possible values of a variable should be listed in the data dictionary, whereas the minimum redundancy hypothesis suggests that only the most important values should be listed multiple times, reducing redundancy in the dictionary."
  },
   {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What are the major sectors impacted by AI?",
    "answer": "AI is making a transformative impact across many sectors. In healthcare, AI applications range from robotic surgeries to virtual nursing assistants. In finance, AI drives algorithms for fraud detection and customer insights. Additionally, in the automotive industry, AI is pivotal in developing self-driving car technology."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Can you give an example of how AI has transformed a traditional industry?",
    "answer": "A great example is the retail industry. AI has revolutionized the sector by enabling personalized shopping experiences through data analytics, optimizing supply chains with predictive modeling, and enhancing customer service through chatbots and automated systems."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is Narrow AI, and what are its typical applications?",
    "answer": "Narrow AI, also known as weak AI, is designed to perform specific tasks. It operates within a limited context and doesn't possess general cognitive abilities. Common applications include voice assistants like Siri and Alexa, recommendation systems on streaming services, and facial recognition software."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Can you explain what General AI is, and how does it differ from Narrow AI?",
    "answer": "General AI, or strong AI, refers to an artificial intelligence that can understand and perform any intellectual task that a human being can. Unlike Narrow AI, which is limited to specific tasks, General AI has broad capabilities that mimic human intelligence. However, General AI remains largely theoretical and has not yet been realized."
  },
   {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "What is the difference between machine learning and deep learning?",
    "answer": "Machine learning algorithms vary from simple to complex, handling tasks from basic classification to dynamic predictions. Deep learning is a specialized subset of machine learning that uses layered neural networks to analyze various factors of complex data. Essentially, all deep learning is machine learning, but not all machine learning is deep learning."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How does the bias-variance trade-off affect model performance?",
    "answer": "In machine learning, the bias-variance trade-off is crucial for model accuracy. High bias can lead a model to miss relevant relationships between features and target outputs (underfitting), while high variance can cause the model to fit too closely to the training data, including noise (overfitting). The goal is to balance these two factors to minimize the overall error."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Can you explain what a loss function is and how it impacts the training of machine learning models?",
    "answer": "A loss function, also known as a cost function, is a critical component in training machine learning models. It quantifies the difference between the model's predicted values and the actual values. During training, the goal is to minimize this loss using optimization techniques such as gradient descent. The choice of loss function can significantly influence how the model's parameters are adjusted and, ultimately, its performance."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What is Generative AI and how is it used in various industries?",
    "answer": "Generative AI refers to technologies that can produce new data instances resembling the training data. This includes generating text, images, videos, and music. It is used in industries such as media and entertainment for creating realistic video game environments and new music compositions, as well as in marketing to generate personalized content that enhances customer engagement."
  },
   {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Can you explain how a Random Forest algorithm differs from a Decision Tree?",
    "answer": "While both Random Forests and Decision Trees are tree-based algorithms, a Random Forest is essentially a collection of Decision Trees designed to overcome the overfitting problem of a single Decision Tree. It achieves this by averaging multiple Decision Trees trained on different subsets of the training data, leading to improved accuracy and robustness."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What are the advantages of using Gradient Boosting algorithms?",
    "answer": "Gradient Boosting is a powerful ensemble technique that builds models sequentially, where each new model corrects the errors made by previous ones. This approach effectively reduces bias and variance, leading to strong predictive performance, especially on complex datasets where single models might struggle with accuracy."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How do you address the challenge of an imbalanced dataset in a machine learning project?",
    "answer": "Handling imbalanced datasets is critical for fair and effective model performance. Common techniques include oversampling the minority class, undersampling the majority class, or using synthetic data generation methods like SMOTE. Additionally, adjusting the decision threshold and employing evaluation metrics such as the F1-score can further help in managing class imbalances."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How would you use SVM for a non-linear classification problem?",
    "answer": "Support Vector Machines (SVMs) can tackle non-linear classification problems using the kernel trick. By applying a kernel function, SVMs map input data into a higher-dimensional feature space where the data points are more likely to be linearly separable, allowing the algorithm to identify an optimal hyperplane for classification."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Can you differentiate between parametric and non-parametric models?",
    "answer": "Parametric models assume a predetermined form for the relationship between inputs and outputs, which simplifies the learning process but can limit flexibility. Non-parametric models, on the other hand, do not assume such a form and can adapt to a wider variety of data patterns, offering more flexibility at the cost of requiring more data to make accurate predictions."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What are some advanced NLP techniques you have used in your projects?",
    "answer": "In my NLP projects, I've implemented advanced techniques such as BERT for understanding context in text, LSTMs for sequence prediction, and attention mechanisms to improve the interpretability and performance of models, especially in tasks like sentiment analysis and text summarization."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "Can you explain what a CNN is and where it might be used?",
    "answer": "A Convolutional Neural Network (CNN) is particularly powerful for tasks involving image data. It uses a mathematical operation called convolution and has been highly successful in fields such as image recognition and classification, powering innovations like facial recognition technologies."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Can you discuss the advantages of using LSTM over traditional RNNs in sequence modeling tasks?",
    "answer": "Long Short-Term Memory networks (LSTMs) are a specialized type of Recurrent Neural Networks (RNNs) designed to address the problem of long-term dependencies, which traditional RNNs often struggle with. While RNNs work well when only recent information is needed, they tend to lose context from earlier data. LSTMs overcome this limitation by using memory cells that retain information for longer periods, making them well-suited for complex sequence prediction tasks such as time series forecasting, natural language processing, and speech recognition."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How would you design an AI system for enhancing customer support?",
    "answer": "To enhance customer support with AI, I would implement a chatbot using NLP techniques to understand and respond to customer queries effectively. The system would be trained on a dataset of customer service interactions to learn various customer requests and the appropriate responses. Additionally, integrating sentiment analysis could help in escalating complex or sensitive issues to human agents."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "In what ways can AI optimize content creation for marketing?",
    "answer": "AI can revolutionize content creation in marketing by generating data-driven content suggestions, personalizing content for different audience segments, and optimizing content delivery times. Tools like GPT (Generative Pre-trained Transformer) can be used to automate routine content creation, freeing up human marketers to focus on strategic and creative tasks."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "Describe a machine learning approach to detect fraudulent transactions.",
    "answer": "To detect fraudulent transactions, I would develop a machine learning model that uses historical transaction data to learn patterns associated with fraud. Techniques such as anomaly detection or supervised learning with labeled fraud cases could be applied. The model would be continuously updated with new transaction data to adapt to evolving fraud techniques."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How can AI be utilized to improve operational efficiency in manufacturing or logistics?",
    "answer": "AI can enhance operational efficiency in manufacturing or logistics through several approaches: Predictive maintenance using sensor data to prevent equipment failures; supply chain optimization with demand forecasting and inventory management algorithms; robotics and automation to speed up repetitive tasks; real-time data analysis to quickly identify and resolve inefficiencies; and AI-driven quality control systems to accurately detect defects. These applications streamline operations, reduce costs, and improve service delivery."
  },
   {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How can AI professionals ensure data privacy when developing AI models?",
    "answer": "AI professionals must prioritize data privacy by implementing data encryption, anonymization techniques, and ensuring that data collection and processing comply with relevant laws and ethical standards. Regular audits and transparency reports can also help maintain trust and accountability."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What steps would you take to make an AI model more transparent?",
    "answer": "To enhance the transparency of an AI model, I would focus on thorough documentation throughout the development process. This includes detailing data sources, preprocessing steps, and the rationale behind algorithm choices, as well as documenting the model's decision-making process."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How do you address biases in AI predictions?",
    "answer": "Addressing biases in AI involves carefully curating representative datasets, applying techniques to detect and correct biases, and continuously monitoring performance across different demographic groups. Regular training on ethical AI practices is also crucial for the team."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What are your thoughts on AI and job displacement?",
    "answer": "While AI can lead to job displacement, it also creates opportunities for new roles. Organizations should invest in employee retraining and education to ease transitions, and policymakers must develop legislation that supports workforce adaptation."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How do Transformers and self-attention mechanisms work in Generative AI?",
    "answer": "Transformers are deep learning models that rely on a mechanism called self-attention, which allows the model to weigh the importance of each word in a sentence relative to all other words. Unlike recurrent models, transformers process the entire input sequence at once, using self-attention to capture long-range dependencies. Self-attention calculates a weighted sum of the input, helping the model focus on relevant parts of the data while ignoring irrelevant details. This approach enables transformers to excel at tasks like text generation, translation, and summarization by understanding context and relationships in the data."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What are the ethical concerns associated with Generative AI technologies?",
    "answer": "Generative AI raises ethical concerns such as the potential for misuse in creating deepfakes, generating misleading or harmful content, and infringing on intellectual property. There are also concerns about biased outputs if the training data contains biases. Ensuring transparency, consent, and accountability are crucial steps in mitigating these ethical risks."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Easy",
    "question": "How can Generative AI be applied in natural language processing (NLP)?",
    "answer": "Generative AI is widely used in NLP for tasks such as text generation, machine translation, summarization, and conversational agents. For example, models like GPT (Generative Pre-trained Transformer) generate coherent, contextually relevant text, enabling chatbots, automated content creation, and personalized responses in customer service."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "What are the main differences between Generative AI and traditional machine learning models?",
    "answer": "Traditional machine learning models focus on making predictions or classifications based on existing data, while Generative AI models create new data instances that resemble the training data. For example, a traditional ML model may classify images as cats or dogs, while a generative model can create new images of cats or dogs. Generative models are more creative in nature, focusing on generating rather than predicting."
  },
  {
    "Category": "Technology",
    "Specialty": "Artificial intelligence",
    "Difficulty": "Medium",
    "question": "How can Generative AI improve data augmentation in machine learning?",
    "answer": "Generative AI can be used to augment datasets by generating synthetic data that closely mimics the original data, which can help improve the performance of machine learning models. For instance, in image recognition tasks, GANs can create realistic images that increase the diversity of training data, reduce overfitting, and enhance the model’s ability to generalize to new data."
  }

]
