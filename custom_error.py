class InvalidBalanceException(Exception):
  def __init__(self, message="Starting balance cannot exceed allowed limit."):
    self.message = message
    super().__init__(self.message)