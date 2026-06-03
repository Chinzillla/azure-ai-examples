# Map Potential Harms

first stage in a responsible generative AI process is to map the potential harms that could affect your planned solution.

Four Steps in this stage:

## 1. Identify potential harms

Potential harms to the specific services and models used to generate output as well as any fine-tuning or grounding data used to customize the outputs.

Common types of potential harm
- generating content that is offensive, pejorative, or discriminatory
- generating content that contains factual inaccuracies
- generating content that encourages or supports illegal or unethical behavior or practicies

We can review guidance: https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Guide.pdf

We can also use the template: https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf

## 2. Prioritize identified harms

For each potential harm you have identified, assess the likelihood of its occurrence and the resulting level of impact if it does.
- use this information to prioritize the harms with the most likely and impactful harms first

prioritization must take into account the intended use of the solution as well as the potential for misuse; and can be subjective

For Example:
```md
you're developing a smart kitchen copilot that provides recipe assistance to chefs and amateur cooks

Potential harms
- The solution provides inaccurate cooking times, resulting in undercooked food that may cause illness.
- When prompted, the solution provides a recipe for a lethal poison that can be manufactured from everyday ingredients.
```

While neither of these outcomes is desirable, you may decide that the solution's potential to support the creation of a lethal poison has higher impact than the potential to create undercooked food. 

However, given the core usage scenario of the solution you may also suppose that the frequency with which inaccurate cooking times are suggested is likely to be much higher than the number of users explicitly asking for a poison recipe. 

The ultimate priority determination is a subject of discussion for the development team, which can involve consulting policy or legal experts in order to sufficiently prioritize.

## 3. Test and verify the prioritized harms

Once you have a prioritized list
- its time to test to make sure the harms occur and if so under what conditions

testing may reveal presence of previously unidentified harms that can be added to the priority list

Common approach:
red team testing - team of testers deliberately probes the solution for weaknesses and attemptes to produce harmful results

example: requesting poison recipes or quick recipes that include ingredients that should be thoroughly cooked

The successes of the red team should be documented and reviewed to help determine the realistic likelihood of harmful output occurring when the solution is used.

Note about red teaming:
```md
Red teaming is a strategy that is often used to find security vulnerabilities or other weaknesses that can compromise the integrity of a software solution. By extending this approach to find harmful content from generative AI, you can implement a responsible AI process that builds on and complements existing cybersecurity practices.

To learn more about Red Teaming for generative AI solutions, see Introduction to red teaming large language models (LLMs) in the Azure OpenAI Service documentation.
```

## 4. Document and share the verified harms

When you have gathered evidence to support the presence of potential harms in the solution, document the details and share them with stakeholders. 

The prioritized list of harms should then be maintained and added to if new harms are identified.