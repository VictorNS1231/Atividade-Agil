from src.media import Media

class Test_Media:

    def test_calculoMedia(self):
        result = Media.calculoMedia(2, 3)
        assert result == 2.5
    
     # E SE FOR DIVISÃO POR ZERO?????????
    def test_divisao_por_zero(self):
        result = Media.calculoMedia(9, 0)
        assert result == 0