# Simplish evaluation cases

Use these prompts to check whether a change produces clearer, accurate, useful answers. They test response quality; they do not measure attention, learning gains, or long-term memory. Equivalent wording and different sound teaching examples are welcome.

Run each prompt in a fresh conversation with Simplish available. Record the assistant and version, model, date, skill revision, full prompt, and response. When checking portability, run the affected cases in each supported assistant and keep the results separate. For a comparison, keep the model and prompt the same. Review the affected cases after a narrow change; use the full set for changes to the general writing or teaching rules.

## Common rubric

Score each applicable dimension from 0 to 2: **0** fails the goal, **1** partly meets it, **2** meets it. Mark a dimension not applicable when the request does not require it. Record a concrete example for any failure or proposed improvement.

| Dimension | A successful response |
|---|---|
| Accuracy and fidelity | Keeps essential facts, conditions, uncertainty, and the meaning of supplied text. |
| Request fit | Answers the actual question at the requested depth and follows the requested format. |
| Reading clarity | Makes the central idea easy to find, uses clear actors and references, and defines necessary unfamiliar terms. |
| Connected reasoning | Explains the important relationships without hidden prerequisites or disconnected fragments. |
| Teaching fit | Adapts to stated knowledge; examples, practice, and feedback serve the learning goal when applicable. |
| Evidence boundaries | Avoids invented sources, unsupported certainty, formal STE compliance claims, and claims to diagnose or optimize a reader's brain. |

A material factual error, changed source meaning, or unsupported effectiveness claim blocks acceptance even if other scores are high. Use scores to locate problems, not to claim a scientifically validated quality measurement.

## 1. Quick answer

**Prompt**

> Why does a metal spoon feel colder than a wooden spoon when both have been in the same room all night? Answer in no more than four sentences.

**Expected outcomes**

- Explains that metal transfers heat away from a warmer hand faster than wood does.
- Distinguishes the sensation from the objects having different temperatures under the stated conditions.
- Meets the length request and avoids an unnecessary lesson, quiz, or action plan.

## 2. Faithful rewrite

**Prompt**

> Rewrite this fictional policy in simple English. Preserve every condition and deadline; do not add advice or change the policy:
>
> “Project owners must submit the release checklist at least two business days before deployment. Security approval is required only when a release changes authentication or handles a new category of personal data. If that approval is required but has not been granted, deployment must be postponed. Emergency fixes may bypass the checklist deadline with the incident commander's written approval, but this exception does not waive required security approval. A retrospective checklist must be submitted within one business day after an emergency deployment.”

**Expected outcomes**

- Keeps the two-business-day deadline and the one-business-day retrospective deadline distinct.
- Preserves the alternative security approval triggers and the requirement to postpone deployment when required approval is missing.
- Limits the emergency exception to the checklist deadline and preserves written approval by the named role.
- Improves readability without silently turning the rewrite into a summary or introducing homework.

## 3. Beginner lesson

**Prompt**

> I understand what one half and one third mean, but I do not understand why I cannot add their numerators and denominators. Teach me how to add 1/2 and 1/3. Explain why each important step works, then give me one optional practice problem with its answer after the question.

**Expected outcomes**

- Explains that the pieces must be the same size before counting them together.
- Connects equivalent fractions to the calculation and obtains 5/6.
- Addresses the proposed incorrect method without shaming the learner.
- Provides one solvable practice problem with a correct, clearly separated answer and enough reasoning to check the method.
- Uses any picture or analogy to explain the mathematics, with an explicit connection to the fractions.

## 4. Explanation for an experienced reader

**Prompt**

> I know how to calculate the mean and median. Explain why a large outlier can change the mean a lot while leaving the median unchanged. Use one small numerical example. Skip definitions I already know and do not add a quiz.

**Expected outcomes**

- Focuses on how the mean uses every value's magnitude and how the median depends on the middle position or positions after sorting.
- Uses correctly calculated before-and-after values that demonstrate the stated effect.
- Preserves the qualification that the median *can* stay unchanged, rather than claiming outliers can never affect it.
- Respects the reader's knowledge and the request to omit a quiz.

## 5. Detailed explanation

**Prompt**

> Give me a detailed explanation, around 900 words, of how photosynthesis and cellular respiration relate. I remember basic school biology but confuse matter with energy. Cover what enters and leaves each process, what plants do during day and night, and a concrete example following carbon through the system. Define technical terms where I need them. Include a comparison table, but no practice questions.

**Expected outcomes**

- Develops the requested explanation in one response with substantive detail near the requested length.
- Distinguishes transformations of matter from transfers and transformations of energy.
- Explains that plants perform cellular respiration during both day and night, while photosynthesis requires light.
- Uses accurate inputs and outputs, a coherent carbon example, and a useful comparison table.
- Connects sections so that the reader can follow the relationship between the processes without relying on unexplained terminology.
- Does not force extreme brevity, omit requested material, add a quiz, or require repeated requests to continue.

## 6. Study plan with realistic limits

**Prompt**

> I have seven days to learn the main ideas of fractions and I can study for 15 minutes each day. I can already identify a numerator and denominator. Make a simple study plan with examples, practice, and later review. I do not want reminders created. Can this guarantee that I will remember everything for six months?

**Expected outcomes**

- Provides a feasible seven-day plan within the daily time budget and starts from the stated knowledge.
- Includes worked examples, learner attempts, checking or feedback, and recall on later days.
- Presents review intervals as adjustable choices and explains how difficulty or success can guide changes.
- Clearly answers that the plan cannot guarantee six-month retention and that later checks would be needed to assess retention.
- Does not create reminders or claim an optimal universal schedule, fixed memory capacity, or personalized brain pattern.

## Review record

For each evaluated change, record:

- The change and the problem it is intended to solve.
- Cases run, assistant and version, model, date, and skill revision.
- Scores with examples of improvements and remaining failures.
- Whether a previous strength regressed, such as accuracy or requested detail.
- The decision to keep, revise, or revert the change.

Keep reusable records free of personal or confidential information. A pleasing response or one successful run is evidence about that output, not proof of learning effectiveness.
