# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "In a set of mutually exclusive rules, an individual case would only satisfy one rule, without any possibility of overlapping or ambiguity. However, in this scenario, the same individual could potentially satisfy multiple rules depending on their combination of attributes. Therefore, the rules provided are not mutually exclusive."
    answers["(b) explain"] = "The rules do not cover all possible scenarios exhaustively. For instance:There's no rule explicitly covering a homeowner (Yes) who is married or divorced. No specific rule for individuals with medium annual income and not currently employed.No rule for individuals with high annual income and currently employed.While some rules might seem to cover broad categories (like Marital Status = Single), they don't address every combination with other attributes (e.g., a single person with high income and employment status).Therefore, the rule set is not exhaustive. There are combinations of attributes for which the outcome (DB = Yes or No) is not determined by the existing rules. In practice, for a rule set to be considered exhaustive, there should be a clear outcome specified for every possible combination of input attribute values."
    answers["(c) explain"] = "These rules are neither mutually exclusive nor exhaustive, as discussed previously. In such a scenario, the order in which the rules are applied can significantly influence the outcome."
    answers["(d) explain"] = " a default class is needed for the rule set, particularly because the rules provided are not exhaustive. An exhaustive rule set would cover every possible combination of attribute values, ensuring that any instance can be classified without ambiguity. However, since there are attribute value combinations not addressed by the current rules, a default class becomes essential."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "A vertebrate cannot be both warm-blooded and cold-blooded.A vertebrate cannot be both aerial and aquatic.If a vertebrate gives birth, it does not fall into the conditions of R1, R2, or R4.Thus, no vertebrate can satisfy the conditions of more than one rule at the same time. The rules are indeed mutually exclusive."
    answers["(b) example"] = "Given these gaps, the rule set is not exhaustive. For it to be exhaustive, there would need to be additional rules to cover these cases,ensuring that every vertebrate can be classified by the rule set. This includes rules for amphibians and any other special cases that don't fit the current rules."
    answers["(c) example"] = "if new rules were added to cover the gaps and make the set exhaustive, or if the existing rules were changed in a way that they are no longer mutually exclusive, then the ordering could become important. In such cases, rules would need to be ordered based on the priority of the conditions or some other logical sequence to ensure correct classification."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = "True"
    answers["(b)"] = "True"
    answers["(c)"] = "False"
    answers["(d)"] = "True"

    # explain_string: explanation in english prose
    answers["(a) explain"] = "During the backward phase, the weight update formula is applied in the reverse direction. In other words, the weights at level k + 1 are updated before the weights at level k are updated. This back-propagation approach allows us touse the errors for neurons at layer k + 1 to estimate the errors for neurons atlayer k.254"
    answers["(b) explain"] = "This forward computation is typical of feed-forward neural networks, where the activations of the current layer are used to compute the activations of the subsequent layer. For each node in layer k+1, the activation is determined by taking the weighted sum of outputs from the nodes in layer k, adding a bias, and then applying an activation function.So, when applying an ANN model to a test instance, the activations at nodes at the k+1th layer indeed rely on and are computed using the activations at nodes at the kth layer."
    answers["(c) explain"] = "The training errors vanishing to zero would typically indicate that the model is learning effectively on the training set. In contrast, large test errors would suggest overfitting, where the model has learned the training data too closely and fails to generalize well to unseen data.The vanishing gradient problem can contribute to poor performance on the training data (particularly affecting deeper layers of the network), not the situation where training errors vanish to zero"
    answers["(d) explain"] = "If yi(k)=y^i(k)  for all training instances, then yi(k)-y^i(k)=0 and therefore the weight update term becomes zero. Since the weight update is zero, the gradients of the loss with respect to the weights at all layers will indeed be 0, which means no further updates to the weights will be made in that iteration."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "no"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.4
    answers["(c) P(X_2=1 | -)"] = 0.5
    answers["(c) P(X_3=1 | +)"] = 0.16
    answers["(c) P(X_3=1 | -)"] = 0.0

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "The plot in figure KNN (a) demonstrates that the clusters are clearly separated, each represented by distinct colors, indicating no overlap between classes. In such scenarios, it's generally best to choose a smaller value for K because the points within each class are tightly grouped together. Specifically, when K is set to 1, the performance tends to be slightly better in this context, as the risk of incorrect classification is low due to the limited number of neighbors considered. This situation presents a better class separation than in scenario A, suggesting that a larger K value, like 50, might not be ideal. Using such a high K could overly generalize the decision boundaries, which is why a smaller K would typically be the preferred choice in this case."
    answers["(b) explain"] = "In figure KNN (b), there is noticeable overlap among the classes, suggesting that individual instances might not accurately represent their class due to noise or overlapping boundaries. In such cases, a larger value of K is advisable because the classifier's decision is influenced by a broader range of neighbors, which helps mitigate the impact of noise. A balanced choice could be K = 5. This setting avoids overly smoothing the decision boundary, a common issue with K = 1, where the model might be overly influenced by outliers. Conversely, K = 5 provides enough detail to accurately reflect the complexities of the actual class boundaries, unlike K = 50, which might oversimplify the decision surface, leading to underfitting. While K = 50 could ignore critical nuances in the data, K = 5 strikes a balance, offering a more nuanced and accurate representation of the data's inherent structure"

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.4
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.4
    answers["(a) P(A=1|-)"] = 0.8
    answers["(a) P(B=1|-)"] = 0.0
    answers["(a) P(C=1|-)"] = 0.4

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "To compute P(Attribute=1∣Class=+), first ascertain the number of times the attribute is 1 when the class is positive (+). This is achieved by counting the instances of the attribute being 1 for all positive class occurrences. For example, if in a dataset, instances 5 and 10 feature the attribute as 1 when the class is positive, note these instances. Next, calculate the total positive class occurrences, such as examples 2, 5, 6, 9, and 10, which add up to five. To determine P(A=1∣+), divide the count of instances where A is 1 in the positive class (2 instances) by the total number of positive cases (5), resulting in P(A=1∣+)= 2/5"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.064
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "In a Naive Bayes framework where each feature value is set to 1, the model predicts the outcome as belonging to the positive class. This leads to the conditional probability of any feature being associated with the negative class to be zero, which in turn results in the overall probability of the negative class being zero. Consequently, this scenario leaves the positive class as the only logical prediction."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.3
    answers["(c) P(A=1,B=1)"] = 0.1

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "no"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.7
    answers["(d) P(A=1,B=0)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "no"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.8
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "yes"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "Essentially, the variables A and B are deemed to be conditionally independent with respect to the class+, a concept rooted in the necessity for such independence when the Naive Bayes classifier's conditional independence stipulations are no longer applicable. This is depicted by the formula where the combined probability of A and B given the class is equivalent to the multiplication of the individual probabilities of A and B given the class, denoted as P(A&B|class) = P(A|class) x P(B|class)."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
