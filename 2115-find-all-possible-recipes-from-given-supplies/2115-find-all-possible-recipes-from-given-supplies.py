class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dependsOn = [0] * len(recipes)
        neighbour = defaultdict(list)
        supplies = set(supplies)
        
        for index,recipe in enumerate((recipes)):
            for ingredient in ingredients[index]:
                if ingredient not in supplies:
                    neighbour[ingredient].append((index,recipe))
                    dependsOn[index] += 1
        queue = deque()
        for index,recipe in enumerate(recipes):
            if dependsOn[index] == 0:
                queue.append(recipe)
        
        while queue:
            ingredient = queue.popleft()
            for index,recipe in neighbour[ingredient]:
                dependsOn[index] -= 1
                if dependsOn[index] == 0:
                    queue.append(recipe)
        ans = []
        for i in range(len(dependsOn)):
            if dependsOn[i] == 0:
                ans.append(recipes[i])
        return ans
            