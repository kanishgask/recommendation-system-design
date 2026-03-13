class RecommendationService:

    def __init__(self):
        self.user_history = {}

    def add_user_activity(self, user_id, item):

        if user_id not in self.user_history:
            self.user_history[user_id] = []

        self.user_history[user_id].append(item)

    def get_recommendations(self, user_id):

        history = self.user_history.get(user_id, [])

        recommendations = []

        for item in history:
            recommendations.append(f"similar_to_{item}")

        return recommendations
