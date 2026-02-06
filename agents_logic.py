class AmuletEngine:
    """
    Головний двигун. Оркестратор "Рою".
    """
    def process_pulse(self, user_signal):
        
        # --- ФАЗА 1: 3 КРОКИ ТУДИ (EXPANSION) ---
        
        # 1. ТАНК (Фільтр Реальності)
        # Перевіряє ресурси користувача (гроші, здоров'я)
        security_status = AgentTank.scan_resources(user_signal)
        if security_status == "CRITICAL":
            return AgentTank.block_action("Not enough mana/resources.")

        # 2. ЛУЧНИК і ХІЛЕР (Паралельний пошук)
        # Лучник шукає факти в базі, Хілер сканує емоційний фон
        logic_vector = AgentArcher.calculate_path(user_signal)
        emotion_aura = AgentHealer.scan_feelings(user_signal)

        # 3. МАГ (Синтез)
        # Створює ідею на основі Логіки та Емоцій
        draft_idea = AgentMage.transmute(logic_vector, emotion_aura)

        # --- ТОЧКА СИНГУЛЯРНОСТІ (3-6-9) ---
        
        # --- ФАЗА 2: 3 КРОКИ НАЗАД (CONTRACTION) ---

        # 4. АСАСІН (Перевірка Тіні)
        # Шукає самообман у ідеї Мага
        truth_check = AgentAssassin.detect_lies(draft_idea)
        
        if not truth_check.is_true:
            return self.recalibrate(draft_idea)

        # 5. КРИСТАЛІЗАЦІЯ (Збірка Кубика)
        final_cube = CubeBuilder.build(
            action=draft_idea, 
            safety=security_status, 
            shadow=truth_check.shadow_insight
        )
        
        return final_cube
